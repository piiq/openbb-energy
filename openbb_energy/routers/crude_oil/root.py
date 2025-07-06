"""Crude Oil Imports router."""

from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel

router = Router(prefix="/crude_oil")


@router.command(model="CrudeOilImports")
async def imports(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Crude Oil Imports by Country and Destination.

    Provides crude oil import data from EIA-814 including:
    - Origin country and destination (refinery/port/state/PADD region)
    - Grade types (Light Sweet, Light Sour, Medium, Heavy Sweet, Heavy Sour)
    - Quantity and aggregation by country/region (including OPEC/non-OPEC groupings)
    """
    return await OBBject.from_query(Query(**locals()))
