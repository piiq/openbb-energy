"""Consumption by End Use Fetcher."""
import warnings
from typing import Any, Dict, List, Optional
from openbb_core.provider.abstract.fetcher import Fetcher
from .consumption import ConsumptionQueryParams, ConsumptionData

from ..utils.helpers import make_eia_params, make_eia_request, process_warnings

_warn = warnings.warn


class ConsumptionNumberOfConsumersFetcher(
    Fetcher[
        ConsumptionQueryParams,
        List[ConsumptionData],
    ]
):
    """Number of consumers Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> ConsumptionQueryParams:
        """Transform query."""
        if params.get("frequency") == "monthly":
            _warn(
                "Number of consumers data does not support monthly frequency. "
                + "Changing frequency to annual."
            )
            params["frequency"] = "annual"
        for key in ["start_date", "end_date"]:
            if params.get(key) and "-" in params[key]:
                year = params[key].split("-")[0]
                _warn(
                    "Number of consumers data does not support monthly frequency. "
                    + f"Changing {key} from {params[key]} to {year}."
                )
                params[key] = year

        return ConsumptionQueryParams(**params)

    @staticmethod
    def extract_data(  # pylint: disable=unused-argument
        query: ConsumptionQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data."""
        api_key = credentials.get("eia_api_key") if credentials else ""

        params = make_eia_params(
            query=query, facet_list=["duoarea", "process", "series"]
        )
        params["api_key"] = api_key

        response = make_eia_request(
            api="natural-gas",
            route1="cons",
            route2="sum",
            api_version=2,
            params=params,
        )
        process_warnings(response["response"])
        data: List[Dict] = response["response"]["data"]
        return data

    @staticmethod
    def transform_data(  # pylint: disable=unused-argument
        query: ConsumptionQueryParams, data: List[dict], **kwargs: Any
    ) -> List[ConsumptionData]:
        """Transform data."""
        for d in data:
            d["period"] = str(d["period"])
        return [ConsumptionData(**d) for d in data]
