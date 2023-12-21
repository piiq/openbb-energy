"""Natural Gas Summary router."""
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


router = Router(prefix="/summary")


@router.command(model="SummarySupplyAndDisposition")
async def supply_and_disposition(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Annual Supply & Disposition by State.

    - Balancing Item volumes are equal to total disposition minus total supply.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="Summary")
async def summary(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Summary.

    - Prices are in nominal dollars.
    - Through 2001, electric power price data are for regulated electric utilities only;
      beginning in 2002, data also include nonregulated members of the electric power
      sector.
    - Monthly preliminary (from January 2018 to present) state-level data for the
      production series, except marketed production, are not available until after the
      final annual reports for this series is collected and processed.
    - Final annual data are generally available in the third quarter of the following
      year.
    - Gas volumes delivered for use as vehicle fuel are included in the State annual
      totals through 2010 but not in the State monthly components.
    - Gas volumes delivered for vehicle fuel are included in the State monthly totals
      from January 2011 forward.
    - As of report year 2021, well count data have been discontinued.
    - The latest natural gas well count data can be found at
      https://www.eia.gov/petroleum/wells/ U.S. Oil and Natural Gas Wells by Production
      Rate.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="SummarySupplyAndDispositionBalance")
async def monthly_supply_and_disposition(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Natural Gas Monthly Supply and Disposition Balance.

    - Balancing item represents quantities lost and imbalances in the data due to
      differences among data sources.
    """
    return await OBBject.from_query(Query(**locals()))
