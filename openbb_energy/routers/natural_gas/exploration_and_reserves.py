"""Natural Gas Exploration and Reserves Router."""
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


router = Router(prefix="/exploration_and_reserves")


@router.command(model="EnRSummary")
async def summary(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Reserves Summary as of Dec. 31.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.  The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRCrudeOilPlusLeaseCondensate")
async def crude_plus_lease(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Crude Oil plus Lease Condensate.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.  The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRDryNaturalGasProvedReserves")
async def dry_natural_gas(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Dry Natural Gas Proved Reserves.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.  The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRNaturalGasProvedReservesWetAfterLeaseSeparation")
async def wals(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Proved Reserves, Wet After Lease Separation.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.  The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRNonassociatedNaturalGasProvedReservesWetAfterLeaseSeparation")
async def wals_na(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Nonassociated Natural Gas Proved Reserves, Wet After Lease Separation.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.  The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="EnRAssociatedDissolvedNaturalGasProvedReservesWetAfterLeaseSeparation"
)
async def wals_ad(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Associated-Dissolved Natural Gas Proved Reserves, Wet After Lease Separation.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.  The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRNaturalGasLiquidsProvedReserves")
async def liquids(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Natural Gas Liquids Proved Reserves.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.  The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="EnREstimatedNaturalGasPlantLiquidsContainedInTotalNaturalGasProvedReserves"
)
async def plant_liquids_in_total(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """
    Estimated Natural Gas Plant Liquids contained in Total Natural Gas Proved Reserves.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.  The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRLeaseCondensate")
async def lease_condensate(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Lease Condensate.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.  The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRCoalbedMethane")
async def coalbed_methane(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """
    Coalbed Methane.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons. The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRShaleGas")
async def shale_gas(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Shale Gas.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRFederalOffshoreGulfOfMexicoProvedReserves")
async def deep_gom(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Federal Offshore Gulf of Mexico Proved Reserves.

    - Includes Federal Offshore Alabama, Louisiana, and Texas.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRProvedNonproducingReserves")
async def nonproducing_reserves(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Proved Nonproducing Reserves.

    - W --  Individual state volumes are withheld to avoid disclosure of operator-level
      reserves data, due to statistical precision requirements, or due to other data
      quality reasons.The individual state volumes are included in the U.S. Total
      volume.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRCrudeOilAndNaturalGasDrillingActivity")
async def drilling_activity(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Crude Oil and Natural Gas Drilling Activity.

    - Rotary Rigs in Operation: Baker Hughes, Inc., Houston, TX,
    - Active Well Service Rig Count: Energy Workforce & Technology Council, Houston, TX.
    - Rotary rigs in operation are reported weekly. Monthly data are averages of 4- or
      5-week reporting periods, not calendar months. Annual data are averages over 52
      or 53 weeks, not calendar year.
    - Published data are rounded to the nearest whole number.
    - Geographic coverage is the 50 States and the District of Columbia.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRCrudeOilAndNaturalGasExploratoryAndDevelopmentWells")
async def well_count(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Crude Oil and Natural Gas Exploratory and Development Wells.

    - Geographic coverage is the 50 States and the District of Columbia.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRMaximumUSActiveSeismicCrewCounts")
async def seismic_crew_counts(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Maximum U.S. Active Seismic Crew Counts.

    - "48 States" is the United States excluding Alaska and Hawaii. "48 States, Offshore"
    are Federal and State Jurisdiction waters of the Gulf of Mexico. Alaska is all
    onshore. Total crews includes crews with unknown survey dimension. Data are reported
    on the first and fifteenth of each month, except January when they are reported only
    on the fifteenth. When semi-monthly values differ for the month, the larger of the
    two values is shown here. Consequently, this table reflects the maximum number of
    crews at work at any time during the month.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRFootageDrilledForCrudeOilAndNaturalGasWells")
async def well_footage_drilled(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """
    Footage Drilled for Crude Oil and Natural Gas Wells.

    - Totals may not equal sum of components due to independent rounding.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRAverageDepthOfCrudeOilAndNaturalGasWells")
async def well_average_depth(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """
    Average Depth of Crude Oil and Natural Gas Wells.

    - Average depth may not equal averaging of components due to independent rounding.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EnRCostsOfCrudeOilAndNaturalGasWellsDrilled")
async def well_costs_drilled(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """
    Costs of Crude Oil and Natural Gas Wells Drilled.

    - *In chained (2000) dollars, calculated by using gross domestic product price deflators.
    """
    return await OBBject.from_query(Query(**locals()))
