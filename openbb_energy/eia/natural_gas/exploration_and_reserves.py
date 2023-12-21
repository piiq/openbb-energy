"""Exploration and Reserves Fetchers."""
from typing import Any, Dict, List, Optional
from .natural_gas import (
    NaturalGasQueryParams,
    # NaturalGasFetcher,
    NaturalGasAnnualFetcher,
)

from ..utils.helpers import make_eia_params, make_eia_request, process_warnings


class EnRCrudeOilPlusLeaseCondensateFetcher(NaturalGasAnnualFetcher):
    """Crude Oil Plus Lease Condensate Fetcher."""

    @staticmethod
    def extract_data(  # pylint: disable=unused-argument
        query: NaturalGasQueryParams,
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
            route1="enr",
            route2="cplc",
            api_version=2,
            params=params,
        )
        process_warnings(response["response"])
        data: List[Dict] = response["response"]["data"]
        return data
