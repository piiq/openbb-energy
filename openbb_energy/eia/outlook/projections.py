"""EIA Outlook Models."""

from datetime import datetime
from datetime import date as dateType
from typing import Any, Dict, List, Literal, Optional, Union

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field, field_validator

from ..utils.helpers import make_eia_params, make_eia_request, process_warnings

AIO_IEO_FACET_LIST = ["history", "scenario", "tableId", "seriesId", "regionId"]


class IEOQueryParams(QueryParams):
    """International Energy Outlook Query Params."""

    release_year: Literal["2017", "2019", "2021", "2023"] = Field(
        description="Release Year"
    )

    start_year: Optional[str] = Field(
        title="Start Year",
        description="Start Year",
        default="2020",
        alias="start",
    )

    end_year: Optional[str] = Field(
        title="End Year",
        description="End Year",
        default="2050",
        alias="end",
    )

    filter_by_history: Literal["projection", "historic"] = Field(
        title="History",
        description="Historic or Projection",
        default=None,
        alias="history",
    )

    filter_by_scenario: Literal[
        "LowZTC",
        "HighMacro",
        "Reference",
        "LowMacro",
        "HighOilPrice",
        "LowOilPrice",
        "HighZTC",
    ] = Field(
        title="Scenario",
        description="""Projection Scenario.
        LowZTC: Low zero-carbon technology cost
        HighMacro: High economic growth
        Reference: Reference
        LowMacro: Low economic growth
        HighOilPrice: High oil price
        LowOilPrice: Low oil price
        HighZTC: High zero-carbon technology cost""",
        default=None,
        alias="scenario",
    )

    filter_by_table: Optional[str] = Field(
        title="Table ID",
        description="Filter by table id. You can provide a comma separated list of table ids.",
        default=None,
        alias="tableId",
    )

    filter_by_series: Optional[str] = Field(
        title="Series ID",
        description="Filter by series id. You can provide a comma separated list of series ids.",
        default=None,
        alias="seriesId",
    )

    filter_by_region: Optional[str] = Field(
        title="Region ID",
        description="Filter by region id. You can provide a comma separated list of region ids.",
        default=None,
        alias="regionId",
    )


class IEOData(Data):
    """IEO  Data."""

    period: dateType = Field(description="Period")
    history: str = Field(description="History")
    scenario: str = Field(description="Scenario")
    scenario_description: str = Field(description="Scenario Description")
    table_id: str = Field(description="Table ID")
    table_name: str = Field(description="Table Name")
    series_id: str = Field(description="Series ID")
    series_name: str = Field(description="Series Name")
    region_id: str = Field(description="Region ID")
    region_name: str = Field(description="Region Name")
    value: Optional[Union[float, str]] = Field(description="Value")
    unit: str = Field(description="Units of measurement")

    @field_validator("period", mode="before")
    def parse_period(cls, value):
        """Parse period string to datetime."""
        try:
            if "-" in value:
                return datetime.strptime(value, "%Y-%m").date()
            return datetime.strptime(value, "%Y").date()
        except ValueError:
            raise ValueError("Period must be in YYYY or YYYY-MM format")

    @field_validator("value", mode="before")
    def parse_value(cls, value):
        """Parse value string to float."""
        if value:
            return float(value)
        return value


class IEOFetcher(Fetcher[IEOQueryParams, List[IEOData]]):
    """IEO Search Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> IEOQueryParams:
        return IEOQueryParams(**params)

    @staticmethod
    def extract_data(  # pylint: disable=unused-argument
        query: IEOQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data."""
        api_key = credentials.get("eia_api_key") if credentials else ""

        params = make_eia_params(query=query, facet_list=AIO_IEO_FACET_LIST)
        params["api_key"] = api_key

        if query.release_year:
            route1 = params["release_year"]
            del params["release_year"]
        else:
            route1 = "2023"  # This is the latest release year at the time of writing

        response = make_eia_request(
            api="ieo",
            route1=route1,
            route2=None,
            api_version=2,
            params=params,
        )
        if "response" in response:
            process_warnings(response["response"])
            data: List[Dict] = response["response"]["data"]
            return data
        if "error" in response:
            raise ValueError(response["error"])
        return []

    @staticmethod
    def transform_data(  # pylint: disable=unused-argument
        query: IEOQueryParams, data: List[dict], **kwargs: Any
    ) -> List[IEOData]:
        """Transform data."""
        return [IEOData(**d) for d in data]
