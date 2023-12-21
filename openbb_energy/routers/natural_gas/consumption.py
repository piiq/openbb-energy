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
    """Natural Gas Consumption by End Use.

    - Gas volumes delivered for use as vehicle fuel are included in the State annual
      totals through 2009 but not in the State monthly components.
    - Estimates of gas volumes delivered for use as vehicle fuel are included in the
      State monthly totals for January 2010 forward.
    - Gas volumes delivered for use as vehicle fuel are included in the State annual
      totals through 2009 but not in the State monthly components.
    - Estimates of gas volumes delivered for use as vehicle fuel are included in the
      State monthly totals for January 2010 forward.
    - The Electric Power Annual publication is typically released after the Natural Gas
      Annual Publication, and as a result, the most recent complete year shown in the
      Natural Gas Annual publication reflects preliminary volumes and prices in the
      electric sector.
    - These preliminary figures are not finalized until the release of the following
      Natural Gas Annual.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ConsumptionNumberOfConsumers")
async def number_of_consumers(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Number of Natural Gas Consumers.

    - Sales consumers buy their gas from the company that delivered it to them.
    - Transported consumers buy their gas from a company other than the one that
      delivered it to them.

    Beginning in 1996, consumption of natural gas for agricultural use was classified
    as industrial use.
    In 1995 and earlier years, agricultural use was classified as commercial use.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ConsumptionShareOfGasDelivered")
async def share_of_gas_delivered(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """
    Share of Total U.S. Natural Gas Delivered to Consumers.

    - Beginning in 1996, consumption of natural gas for agricultural use was classified
      as industrial use.
    - In 1995 and earlier years, agricultural use was classified as commercial use.
    - From 1967 through 1979, data for the District of Columbia are included with data
      for Maryland.
    - From 1967 through 1979, data for New Hampshire and Vermont are included with data
      for Maine.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ConsumptionAccountOfOthers")
async def account_of_others(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """
    Natural Gas Delivered for the Account of Others.

    - Natural gas that is "delivered for the account of others" is gas that is not owned
      by the company that delivers it to the consumer.
    - Beginning in 1996, consumption of natural gas for agricultural use was classified
      as industrial use.
    - In 1995 and earlier years, agricultural use was classified as commercial use.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ConsumptionHeatContent")
async def heat_content(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """
    Heat Content of Natural Gas Consumed.
    """
    return await OBBject.from_query(Query(**locals()))
