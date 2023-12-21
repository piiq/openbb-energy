"""EIA API helpers."""
import warnings
from typing import Dict, List, Optional

import requests
from openbb_core.provider.abstract.query_params import QueryParams

_warn = warnings.warn

BASE_URL = "https://api.eia.gov"


def make_eia_params(query: QueryParams, facet_list: List[str]):
    """Make EIA API parameters. This includes applying filters."""
    params = query.model_dump(by_alias=True, exclude_none=True)
    params["data[0]"] = "value"

    for facet in facet_list:
        if facet in params:
            for facet_value in params[facet].split(","):
                params[f"facets[{facet}][]"] = facet_value.strip()
            params.pop(facet)
    return params


def make_eia_request(
    api: str,
    route1: str,
    route2: Optional[str],
    api_version: int,
    params: Dict,
) -> Dict:
    """Return a URL for the EIA API.

    Parameters
    ----------
    api : str
        API name.
    route1 : str
        First route.
    route2 : Optional[str]
        Second route.
    api_version : int
        API version.
    params : Dict
        Query parameters.
    exclude : Optional[List[str]]
        Parameters to exclude from query.

    Returns
    -------
    Dict
        JSON response.
    """
    route_url = f"{route1}/{route2}" if route2 else route1
    data_url = (
        BASE_URL + f"/v{str(api_version)}" + f"/{api}" + f"/{route_url}" + "/data"
    )
    r = requests.get(
        data_url,
        params=params,
        headers={"Accept": "application/json"},
        timeout=60,
    )
    return r.json()


def process_warnings(response: Dict) -> None:
    """Process warnings."""
    if "warnings" in response and len(response["warnings"]) > 0:
        for warning in response["warnings"]:
            if warning["warning"] == "incomplete return":
                _warn(
                    f"{warning['warning']} : {warning['description']}. "
                    + f"Total rows available: {response['total']}."
                )
