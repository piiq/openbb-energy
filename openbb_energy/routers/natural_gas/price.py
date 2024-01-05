"""Natural Gas Price router."""
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


router = Router(prefix="/price")


@router.command(model="PriceSummary")
async def summary(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Prices.

    - Prices are in nominal dollars.
    - Gas volumes delivered for use as vehicle fuel are included in the State annual
      totals through 2009 but not in the State monthly components.
    - Through 2001, electric power price data are for regulated electric utilities only;
      beginning in 2002, data also include non-regulated members of the electric power
      sector.
    - Gas volumes delivered for use as vehicle fuel are included in the State annual
      totals through 2009 but not in the State monthly components.
    - Estimates of gas volumes delivered for use as vehicle fuel are included in the
      State monthly totals for January 2010 forward.
    - Preliminary electric power data for 2016 are shown as of the September 2017
      Electric Power Monthly. They will not reflect revisions made in the 2016 Electric
      Power Annual, which was published after the 2016 Natural Gas Annual was released.
      Revised electric power data for 2016 will not be adjusted in the Natural Gas
      Monthly until the 2017 Natural Gas Annual is published.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="PriceFutures")
async def futures(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Spot and Futures Prices (NYMEX).

    - Prices are based on delivery at the Henry Hub in Louisiana.
    - Official daily closing prices at 2:30 p.m. from the trading floor of the New York
      Mercantile Exchange (NYMEX) for a specific delivery month.
    - The natural gas liquids (NGPL) composite price is derived from daily Bloomberg
      spot price data for natural gas liquids at Mont Belvieu, Texas, weighted by gas
      processing plant production volumes of each product as reported on Form EIA-816,
      "Monthly Natural Gas Liquids Report."
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="PriceResidentialCommercial")
async def residential_commercial(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Average Price of Natural Gas Delivered to Residential and Commercial Consumers.

     Delivered by local distribution and marketers in Selected States.

    - Prices are in nominal dollars.
    - Average prices are calculated by weighting percent sold by local distribution
      companies versus percent sold by marketers according to volumes reported on Form
      EIA-176, "Annual Report of Natural and Supplemental Gas Supply and Disposition."
    """
    return await OBBject.from_query(Query(**locals()))
