"""Natural Gas Storage router."""
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


router = Router(prefix="/storage")


@router.command(model="StorageWeeklyWorkingGasUnderground")
async def underground_weekly(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Weekly Working Gas in Underground Storage.

    This table tracks U.S. natural gas inventories held in underground storage facilities.
    The weekly stocks generally are the volumes of working gas as of the report date.
    Changes in reported stock levels reflect all events affecting working gas in storage,
    including injections, withdrawals, and reclassifications between base and working gas,
    including information on estimated measures of sampling variability for the most
    current published estimates of weekly stocks and their net changes.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="StorageUndergroundNaturalGasStorageByAllOperators")
async def underground_all(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Underground Natural Gas Storage by All Operators.

    Change in Working Gas from Same Period, Previous Year, includes data for Alaska which
    had no working gas recorded for periods prior to January 2013.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="StorageUndergroundNaturalGasStorageByStorageType")
async def underground_type(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Underground Natural Gas Storage by Storage Type.

    - Positive net withdrawals indicate the volume of withdrawals in excess of injections.
    - Negative net withdrawals indicate the volume of injections in excess of withdrawals.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="StorageLiquefiedNaturalGasAdditionsToAndWithdrawalsFromStorage")
async def lng_additions_withdrawals(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Liquefied Natural Gas Additions to and Withdrawals from Storage.

    - Positive net withdrawals indicate the volume of withdrawals in excess of injections.
    - Negative net withdrawals indicate the volume of injections in excess of withdrawals.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="StorageUndergroundNaturalGasStorageCapacity")
async def underground_capacity(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Underground Natural Gas Storage Capacity.

    Existing fields include both active and inactive fields.
    """
    return await OBBject.from_query(Query(**locals()))
