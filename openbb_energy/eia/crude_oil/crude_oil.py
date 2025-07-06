"""EIA Crude Oil Import Models."""

import warnings
from datetime import date as dateType
from typing import Any, Dict, List, Literal, Optional

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field, field_validator

from .constants import ORIGIN_IDS, DESTINATION_IDS, OriginIdType, DestinationIdType

_warn = warnings.warn

CRUDE_OIL_FACET_LIST = [
    "originId",
    "originType",
    "destinationId",
    "destinationType",
    "gradeId",
]


class CrudeOilImportsQueryParams(QueryParams):
    """Crude Oil Imports query parameters."""

    frequency: Literal["monthly", "annual"] = Field(
        description="Frequency of the data to be returned.",
        default="monthly",
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

    filter_by_origin_id: Optional[OriginIdType] = Field(
        description="Filter by origin ID. You can provide a comma separated list of origin IDs."
        + " Examples: CTY_CA (Canada), CTY_SA (Saudi Arabia), REG_ME (Middle East)."
        + " Available values can be found in ORIGIN_IDS constant.",
        default=None,
        alias="originId",
    )

    filter_by_origin_type: Optional[Literal["REG", "CTY", "OPN", "WORLD"]] = Field(
        description="Filter by origin type. You can provide a comma separated list of origin types."
        + " Choose from: REG (Region), CTY (Country), OPN (OPEC/non-OPEC), WORLD (World).",
        default=None,
        alias="originType",
    )

    filter_by_destination_id: Optional[DestinationIdType] = Field(
        description="Filter by destination ID. You can provide a comma separated list of destination IDs."
        + " Examples: RF_394 (refinery), PT_1003 (port), PS_LA (state)."
        + " Available values can be found in DESTINATION_IDS constant.",
        default=None,
        alias="destinationId",
    )

    filter_by_destination_type: Optional[
        Literal["PS", "US", "RP", "PP", "RS", "PT", "RF"]
    ] = Field(
        description="Filter by destination type. You can provide a comma separated list of destination types."
        + " Choose from: PS (Port State), US (United States), RP (Refinery PADD), PP (Port PADD), RS (Refinery State), PT (Port), RF (Refinery).",
        default=None,
        alias="destinationType",
    )

    filter_by_grade_id: Optional[Literal["HSW", "MED", "HSO", "LSO", "LSW"]] = Field(
        description="Filter by grade ID. You can provide a comma separated list of grade IDs."
        + " Choose from: HSW (Heavy Sweet), MED (Medium), HSO (Heavy Sour), LSO (Light Sour), LSW (Light Sweet).",
        default=None,
        alias="gradeId",
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

    @field_validator("filter_by_origin_id", mode="before")
    @classmethod
    def validate_origin_id(cls, value):
        """Validate origin ID against available values."""
        if value is not None:
            # Handle comma-separated values
            values = (
                [v.strip() for v in str(value).split(",")]
                if "," in str(value)
                else [str(value)]
            )
            for v in values:
                if v not in ORIGIN_IDS:
                    raise ValueError(
                        f"Invalid origin ID: {v}. Must be one of {ORIGIN_IDS}"
                    )
        return value

    @field_validator("filter_by_destination_id", mode="before")
    @classmethod
    def validate_destination_id(cls, value):
        """Validate destination ID against available values."""
        if value is not None:
            # Handle comma-separated values
            values = (
                [v.strip() for v in str(value).split(",")]
                if "," in str(value)
                else [str(value)]
            )
            for v in values:
                if v not in DESTINATION_IDS:
                    raise ValueError(
                        f"Invalid destination ID: {v}. Must be one of {DESTINATION_IDS}"
                    )
        return value


class CrudeOilImportsData(Data):
    """EIA crude oil imports data."""

    period: dateType = Field(description="Date representing the period.")
    origin_id: Optional[str] = Field(
        description="Origin ID", alias="originId", default=None
    )
    origin_name: Optional[str] = Field(
        description="Origin Name", alias="origin-name", default=None
    )
    origin_type_id: Optional[str] = Field(
        description="Origin Type ID", alias="originType", default=None
    )
    origin_type_name: Optional[str] = Field(
        description="Origin Type Name", alias="originType-name", default=None
    )
    destination_id: Optional[str] = Field(
        description="Destination ID", alias="destinationId", default=None
    )
    destination_name: Optional[str] = Field(
        description="Destination Name", alias="destination-name", default=None
    )
    destination_type_id: Optional[str] = Field(
        description="Destination Type ID", alias="destinationType", default=None
    )
    destination_type_name: Optional[str] = Field(
        description="Destination Type Name", alias="destinationType-name", default=None
    )
    grade_id: Optional[str] = Field(
        description="Grade ID", alias="gradeId", default=None
    )
    grade_name: Optional[str] = Field(
        description="Grade Name", alias="grade-name", default=None
    )
    value: Optional[float] = Field(description="Import volume in thousand barrels")
    units: Optional[str] = Field(
        description="Units of measurement", default="thousand barrels"
    )

    @field_validator("period", mode="before")
    @classmethod
    def validate_period(cls, value):
        """Parse period string to date."""
        if isinstance(value, str):
            from datetime import datetime

            if len(value) == 4:  # Annual data: YYYY
                return datetime.strptime(value, "%Y").date()
            elif len(value) == 7:  # Monthly data: YYYY-MM
                return datetime.strptime(value, "%Y-%m").date()
        return value


class CrudeOilImportsFetcher(
    Fetcher[CrudeOilImportsQueryParams, List[CrudeOilImportsData]]
):
    """Transform the query, extract and transform the data from the EIA API."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CrudeOilImportsQueryParams:
        """Transform the query params."""
        return CrudeOilImportsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: CrudeOilImportsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data from EIA API. To be implemented by specific fetchers."""
        raise NotImplementedError("Subclasses must implement extract_data method")

    @staticmethod
    def transform_data(
        query: CrudeOilImportsQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[CrudeOilImportsData]:
        """Transform the data to the desired format."""
        return [CrudeOilImportsData.model_validate(d) for d in data]


class CrudeOilImportsAnnualFetcher(CrudeOilImportsFetcher):
    """Annual Crude Oil Imports Base Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CrudeOilImportsQueryParams:
        """Transform the query params - override frequency to annual."""
        transformed_params = CrudeOilImportsQueryParams(**params)
        transformed_params.frequency = "annual"
        return transformed_params
