"""Natural Gas Imports and Exports/Pipelines router."""
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


router = Router(prefix="/imports_and_exports")


@router.command(model="InEImportsByCountry")
async def imports(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Natural Gas Imports by Country.

    - Prices for LNG imports are reported as "landed," received at the terminal, or
      "tailgate," after regasification at the terminal.
    - Generally, the reporting of LNG import prices varies by point of entry, and the
      average prices are calculated from a combination of both types of prices.
    - For the "Other" area the point of origin for volumes of imported LNG was unassigned
      in the reports to the Office of Fossil Energy.
    - CNG = Compressed Natural Gas: Natural gas compressed to a pressure at or above
      200-248 bar (i.e., 2900-3600 pounds per square inch) and stored in high-pressure
      containers.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="InEExportsByCountry")
async def exports(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Natural Gas Exports and Re-Exports by Country.

    - The price of LNG exports to Japan is the "landed" price, defined as received at the
      terminal in Japan.
    - CNG = Compressed Natural Gas: Natural gas compressed to a pressure at or above
      200-248 bar (i.e., 2900-3600 pounds per square inch) and stored in high-pressure
      containers.
    - LNG re-exports are shipments of LNG to foreign countries that were previously
      imported, offloaded.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="InEImportsExportsByState")
async def state(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Natural Gas Imports & Exports by State.

    - Prices for LNG imports are reported as "landed," defined as received at the
      terminal, or "tailgate," defined as after regasification at the terminal.
    - Generally, all prices for shipments received at Everett, MA, are reported as landed
      and at Lake Charles, LA, as tailgate.
    - Estimates for Canadian pipeline volumes are derived from the Office of Fossil
      Energy, Natural Gas Imports and Exports, and EIA estimates of dry natural gas
      imports.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="InEImportsByPointOfEntry")
async def imports_by_poe(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Natural Gas Imports by Point of Entry.

    - LNG imports from Canada are delivered by truck.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="InEExportsByPointOfExit")
async def exports_by_poe(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """U.S. Natural Gas Exports and Re-Exports by Point of Exit.

    - LNG exports to Canada and Mexico are delivered by truck.
    - LNG shipments from Kenai Alaska are LNG exports.
    - Pipeline exports to Mexico for April 2015 at Clint and Rio Grande City in Texas were
      estimated
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="InEInternationalInterstateMovementsByState")
async def international_and_interstate(  # pylint: disable=unused-argument
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """International & Interstate Movements of Natural Gas by State.

    - Totals may not equal sum of components due to independent rounding.
    """
    return await OBBject.from_query(Query(**locals()))
