"""Natural Gas Production router."""
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


router = Router(prefix="/production")


@router.command(model="ProductionProducingOilWells")
async def oil_wells(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Number of Gas Producing Oil Wells.

    Well counts include any well that produced natural gas at any time during the
    calendar year.  For most states, \"Oil Wells\" refers only to oil wells that produce
    natural gas (a subset of all oil wells). However, oil well counts for Illinois,
    Indiana, and Kentucky (derived from World Oil) include all oil wells. As of report
    year 2021, well count data have been discontinued. The latest natural gas well count
    data can be found at https://www.eia.gov/petroleum/wells/.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ProductionAndGrossWithdrawalsGross")
async def withdrawals_and_production(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Gross Withdrawals and Production.

    - Beginning with 2006, "Other States" volumes for the production series include the
      following states/areas: Alabama, Arizona, Florida, Idaho, Illinois, Indiana,
      Kentucky, Maryland, Michigan, Mississippi, Missouri, Nebraska, Nevada, New York,
      Oregon, South Dakota, Tennessee, and Virginia.
    - Federal Offshore Pacific is included in California through 2020, and in "Other
      States" starting in 2021.
    - Production series data for 2021 forward are estimates. Final 2021 state-level
      production series data will not be available until the 2021 Natural Gas Annual is
      published (scheduled for the third quarter of 2022).
    - Gross withdrawal volumes in Florida fluctuate from year to year because
      nonhydrocarbon gases are occasionally included in gross withdrawals.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ProductionWellheadValueAndMarketed")
async def value_and_marketed_production(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Wellhead Value and Marketed Production.

    - A number of states reported values associated with production volumes other than
      marketed production.
    - Prior to 1997, state production for Texas, Louisiana, and Alabama includes a
      portion of the Federal Offshore Gulf of Mexico production.
    - Production for these states prior to 1997 excluding the Federal Offshore Gulf of
      Mexico can be found at the state energy data system.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ProductionOffshoreGrossWithdrawals")
async def offshore_withdrawals(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Offshore Gross Withdrawals of Natural Gas.

    - Totals may not equal sum of components due to independent rounding.
    - Federal Offshore Gulf of Mexico production volumes are presented as a separate data
      series beginning in 2001. Production data for the Gulf of Mexico for years prior to
      2001 are presented as part of the production volumes for the States of Alabama,
      Louisiana and Texas.
    - Prior to 1997, state production for Texas, Louisiana, and Alabama includes a
      portion of the Federal Offshore Gulf of Mexico production.
    - Production for these states prior to 1997 excluding the Federal Offshore Gulf of
      Mexico can be found at the state energy data system.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ProductionGulfOfMexicoFederalOffshore")
async def gom_federal_offshore(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Gulf of Mexico Federal Offshore Production.

    - Federal Offshore Gulf of Mexico production volumes are presented as a separate data
      series beginning in 2001. Production data for the Gulf of Mexico for years prior to
      2001 are presented as part of the production volumes for the States of Alabama,
      Louisiana and Texas.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ProductionNaturalGasPlantLiquids")
async def plant_liquids(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Plant Liquids Production.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.  The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ProductionLeaseCondensate")
async def lease_condensate(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Lease Condensate Production.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.  The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ProductionCoalbedMethane")
async def coalbed_methane(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Coalbed Methane Production.

    - Coalbed Methane production data collected in conjunction with proved reserves data
      on Form EIA-23 are unofficial.  Official Coalbed Methane production data from Form
      EIA-895 can be found in Natural Gas Gross Withdrawals and Production.
    - *Eastern States includes Virginia prior to 2006.
    - Other States includes Oklahoma, Pennsylvania, Utah, Virginia, West Virginia, and
      Wyoming for data prior to 2000. These states are individually listed or grouped in
      Eastern States and Western States for 2000 and later.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ProductionShaleGas")
async def shale_gas(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Shale Gas Production.

    - Shale Gas production data collected in conjunction with proved reserves data on
      Form EIA-23 are unofficial. Official Shale Gas production data from Form EIA-895
      can be found in Natural Gas Gross Withdrawals and Production.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ProductionSupplementalGasSupplies")
async def supplemental_gas(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Supplemental Gas Supplies."""
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ProductionProducingGasWells")
async def gas_wells(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Number of Producing Gas Wells.

    - Prior to 2001, the well counts for Federal Offshore Gulf of Mexico were included in
      the well counts for Alabama, Louisiana, and Texas.
    - Well data derived from Enverus, except for Illinois, Indiana, and Kentucky; for
      these states, data are from World Oil and consist of all gas wells and all oil
      wells.
    - As of report year 2021, well count data have been discontinued. The latest natural
      gas well count data can be found at https://www.eia.gov/petroleum/wells/.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ProductionNaturalGasPlantProcessing")
async def plant_processing(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Plant Processing."""
    return await OBBject.from_query(Query(**locals()))
