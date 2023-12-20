"""OpenBB Energy router."""
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


router = Router(prefix="/consumption")


@router.command(model="ConsumptionByEndUse")
async def end_use(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Consumption by End Use."""
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ConsumptionNumberOfConsumers")
async def number_of_consumers(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Consumption Summary."""
    return await OBBject.from_query(Query(**locals()))
