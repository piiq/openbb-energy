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


router = Router(prefix="/imports")


@router.command(model="CrudeOilImportsByCountryAndDestination")
async def by_country_and_destination(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Crude Oil Imports by Country and Destination.

    Provides crude oil import data including origin country, destination refinery/port,
    grade type, and quantity. Source: EIA-814.
    Includes type, grade, quantity by destination.
    
    Interactive data product: www.eia.gov/petroleum/imports/companylevel/
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="CrudeOilImportsByCountry")
async def by_country(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Crude Oil Imports by Country.

    Provides crude oil import data aggregated by origin country.
    Shows imports from various countries and regions including OPEC/non-OPEC groupings.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="CrudeOilImportsByDestination")
async def by_destination(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Crude Oil Imports by Destination.

    Provides crude oil import data aggregated by destination including refineries,
    ports, states, and PADD regions.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="CrudeOilImportsByGrade")
async def by_grade(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Crude Oil Imports by Grade.

    Provides crude oil import data aggregated by grade type including:
    - Light Sweet (LSW)
    - Light Sour (LSO) 
    - Medium (MED)
    - Heavy Sweet (HSW)
    - Heavy Sour (HSO)
    """
    return await OBBject.from_query(Query(**locals()))