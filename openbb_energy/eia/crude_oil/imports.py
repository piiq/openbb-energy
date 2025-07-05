"""Crude Oil Imports Data Fetchers."""

from typing import Any, Dict, List, Optional

from ..utils.helpers import make_eia_params, make_eia_request, process_warnings
from .crude_oil import (
    CrudeOilImportsQueryParams,
    CrudeOilImportsFetcher,
    CrudeOilImportsAnnualFetcher,
    CRUDE_OIL_FACET_LIST,
)


class CrudeOilImportsByCountryAndDestinationFetcher(CrudeOilImportsFetcher):
    """Crude Oil Imports by Country and Destination Fetcher."""

    @staticmethod
    def extract_data(  # pylint: disable=unused-argument
        query: CrudeOilImportsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data."""
        api_key = credentials.get("eia_api_key") if credentials else ""

        params = make_eia_params(query=query, facet_list=CRUDE_OIL_FACET_LIST)
        params["api_key"] = api_key

        response = make_eia_request(
            api="crude-oil-imports",
            route1=None,
            route2=None,
            api_version=2,
            params=params,
        )

        if "response" in response:
            process_warnings(response["response"])
            data: List[Dict] = response["response"]["data"]
            return data
        elif "error" in response:
            raise ValueError(response["error"])


class CrudeOilImportsByCountryFetcher(CrudeOilImportsFetcher):
    """Crude Oil Imports by Country Fetcher - simplified version filtering by origin only."""

    @staticmethod
    def extract_data(  # pylint: disable=unused-argument
        query: CrudeOilImportsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data."""
        api_key = credentials.get("eia_api_key") if credentials else ""

        params = make_eia_params(query=query, facet_list=CRUDE_OIL_FACET_LIST)
        params["api_key"] = api_key

        # Focus on origin filters for country-based queries
        response = make_eia_request(
            api="crude-oil-imports",
            route1=None,
            route2=None,
            api_version=2,
            params=params,
        )

        if "response" in response:
            process_warnings(response["response"])
            data: List[Dict] = response["response"]["data"]
            return data
        elif "error" in response:
            raise ValueError(response["error"])


class CrudeOilImportsByDestinationFetcher(CrudeOilImportsFetcher):
    """Crude Oil Imports by Destination Fetcher - focusing on destination filters."""

    @staticmethod
    def extract_data(  # pylint: disable=unused-argument
        query: CrudeOilImportsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data."""
        api_key = credentials.get("eia_api_key") if credentials else ""

        params = make_eia_params(query=query, facet_list=CRUDE_OIL_FACET_LIST)
        params["api_key"] = api_key

        response = make_eia_request(
            api="crude-oil-imports",
            route1=None,
            route2=None,
            api_version=2,
            params=params,
        )

        if "response" in response:
            process_warnings(response["response"])
            data: List[Dict] = response["response"]["data"]
            return data
        elif "error" in response:
            raise ValueError(response["error"])


class CrudeOilImportsByGradeFetcher(CrudeOilImportsFetcher):
    """Crude Oil Imports by Grade Fetcher - focusing on grade filters."""

    @staticmethod
    def extract_data(  # pylint: disable=unused-argument
        query: CrudeOilImportsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data."""
        api_key = credentials.get("eia_api_key") if credentials else ""

        params = make_eia_params(query=query, facet_list=CRUDE_OIL_FACET_LIST)
        params["api_key"] = api_key

        response = make_eia_request(
            api="crude-oil-imports",
            route1=None,
            route2=None,
            api_version=2,
            params=params,
        )

        if "response" in response:
            process_warnings(response["response"])
            data: List[Dict] = response["response"]["data"]
            return data
        elif "error" in response:
            raise ValueError(response["error"])