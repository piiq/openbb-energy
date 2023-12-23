"""EIA Natural Gas Consumption Summary Fetcher for OpenBB Energy."""
import warnings
from typing import Literal, Optional, List, Any, Dict, Union

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field

_warn = warnings.warn

NATURAL_GAS_FACET_LIST = ["duoarea", "process", "series"]


class NaturalGasQueryParams(QueryParams):
    """Natural Gas query."""

    frequency: Literal["monthly", "annual"] = Field(
        description="Frequency of the data to be returned.",
        default="annual",
    )

    start_date: Optional[str] = Field(
        description="Start date of the data to be returned."
        + " Format: YYYY for annual data, YYYY-MM for monthly data.",
        default=None,
        alias="start",
    )

    end_date: Optional[str] = Field(
        description="End date of the data to be returned."
        + " Format: YYYY for annual data, YYYY-MM for monthly data.",
        default=None,
        alias="end",
    )

    filter_by_area: Optional[str] = Field(
        description="Filter by area. You can provide a comma separated list of areas."
        + " Choose from:"
        + " SNE (USA-NE), SNY (NEW YORK), SVT (USA-VT), SID (USA-ID),"
        + " SIA (USA-IA), SOH (OHIO), SGA (USA-GA), SWA (WASHINGTON),"
        + " SOR (USA-OR), SIL (USA-IL), SND (USA-ND), SUT (USA-UT),"
        + " SWY (USA-WY), SNV (USA-NV), SNM (USA-NM), SME (USA-ME),"
        + " SCA (CALIFORNIA), SWI (USA-WI), SCT (USA-CT), SSC (USA-SC),"
        + " SNH (USA-NH), SVA (USA-VA), SKS (USA-KS), SKY (USA-KY), SSD (USA-SD),"
        + " SAR (USA-AR), SDE (USA-DE), SAL (USA-AL), SMS (USA-MS), SFL (FLORIDA),"
        + " SWV (USA-WV), SHI (USA-HI), SMI (USA-MI), SMN (MINNESOTA), STN (USA-TN),"
        + " SDC (USA-DC), SOK (USA-OK), SNC (USA-NC), SMT (USA-MT), SMD (USA-MD),"
        + " SRI (USA-RI), SAK (USA-AK), SCO (COLORADO), NUS (U.S.), SMA (MASSACHUSETTS),"
        + " SMO (USA-MO), STX (TEXAS), SNJ (USA-NJ), SIN (USA-IN), SAZ (USA-AZ),"
        + " SPA (USA-PA), SLA (USA-LA)",
        default=None,
        alias="duoarea",
    )

    filter_by_process: Optional[
        Literal["VCS", "VDV", "VRS", "VGT", "VEU", "VIN", "VGP", "VGL"]
    ] = Field(
        description="Filter by process. You can provide a comma separated list of processes."
        + " Choose from:"
        + " VCS (Commercial Consumption),"
        + " VDV (Vehicle Fuel Consumption),"
        + " VRS (Residential Consumption),"
        + " VGT (Delivered to Consumers),"
        + " VEU (Electric Power Consumption),"
        + " VIN (Industrial Consumption),"
        + " VGP  (Pipeline Fuel Consumption)"
        + " and VGL (Lease and Plant Fuel Consumption)",
        default=None,
        alias="process",
    )

    filter_by_series: Optional[str] = Field(
        description="Filter by series id. You can provide a comma separated list of series ids.",
        default=None,
        alias="series",
    )

    limit: Optional[int] = Field(
        description="Limit the number of results returned (5000 max).",
        default=None,
        alias="length",
    )

    offset: Optional[int] = Field(
        description="Offset the results returned."
        + " This is used in conjunction with limit for pagination.",
        default=None,
    )


class NaturalGasData(Data):
    """EIA natural gas survey data."""

    period: str = Field(description="Period")
    area: str = Field(description="Area ID", alias="duoarea")
    area_name: str = Field(description="Area Name", alias="area-name")
    product: str = Field(description="Product ID")
    product_name: str = Field(description="Product Name", alias="product-name")
    process: str = Field(description="Process ID")
    process_name: str = Field(description="Process Name", alias="process-name")
    series: str = Field(description="Series ID")
    series_description: str = Field(
        description="Series Description", alias="series-description"
    )
    value: Optional[Union[float, str]] = Field(description="Value")
    units: str = Field(description="Units of measurement")


class NaturalGasBaseFetcher(
    Fetcher[
        NaturalGasQueryParams,
        List[NaturalGasData],
    ]
):
    """Natural Gas Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> NaturalGasQueryParams:
        """Transform query."""
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    def extract_data(  # pylint: disable=unused-argument
        query: NaturalGasQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data."""
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    def transform_data(  # pylint: disable=unused-argument
        query: NaturalGasQueryParams, data: List[dict], **kwargs: Any
    ) -> List[NaturalGasData]:
        """Transform data."""
        for d in data:
            d["period"] = str(d["period"])
        return [NaturalGasData(**d) for d in data]


# pylint: disable=abstract-method
class NaturalGasFetcher(NaturalGasBaseFetcher):
    """Natural Gas Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> NaturalGasQueryParams:
        """Transform query."""
        return NaturalGasQueryParams(**params)


# pylint: disable=abstract-method
class NaturalGasAnnualFetcher(NaturalGasBaseFetcher):
    """Natural Gas Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> NaturalGasQueryParams:
        """Transform query."""
        if params.get("frequency") == "monthly":
            _warn(
                "This data point does not support monthly frequency. "
                + "Changing frequency to annual."
            )
            params["frequency"] = "annual"
        for key in ["start_date", "end_date"]:
            if params.get(key) and "-" in params[key]:
                year = params[key].split("-")[0]
                _warn(
                    "This data point does not support monthly frequency. "
                    + f"Changing {key} from {params[key]} to {year}."
                )
                params[key] = year

        return NaturalGasQueryParams(**params)
