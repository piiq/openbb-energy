"""Consumption Data Fetchers."""
from typing import Any, Dict, List, Optional

from ..utils.helpers import make_eia_params, make_eia_request, process_warnings
from .natural_gas import (
    NaturalGasQueryParams,
    NaturalGasFetcher,
    NaturalGasMonthlyFetcher,
    NATURAL_GAS_FACET_LIST,
)


class ConsumptionByEndUseFetcher(NaturalGasFetcher):
    """Consumption by End Use Fetcher."""

    @staticmethod
    def extract_data(  # pylint: disable=unused-argument
        query: NaturalGasQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data."""
        api_key = credentials.get("eia_api_key") if credentials else ""

        params = make_eia_params(query=query, facet_list=NATURAL_GAS_FACET_LIST)
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


class ConsumptionNumberOfConsumersFetcher(NaturalGasMonthlyFetcher):
    """Number of consumers Fetcher."""

    @staticmethod
    def extract_data(  # pylint: disable=unused-argument
        query: NaturalGasQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data."""
        api_key = credentials.get("eia_api_key") if credentials else ""

        params = make_eia_params(query=query, facet_list=NATURAL_GAS_FACET_LIST)
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
