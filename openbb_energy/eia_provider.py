"""EIA Data Provider for OpenBB Energy."""

from openbb_core.provider.abstract.provider import Provider

from .eia.natural_gas.consumption import (
    ConsumptionByEndUseFetcher,
    ConsumptionNumberOfConsumersFetcher,
    ConsumptionShareOfGasDeliveredFetcher,
    ConsumptionAccountOfOthersFetcher,
    ConsumptionHeatContentFetcher,
)
from .eia.natural_gas.exploration_and_reserves import (
    EnRCrudeOilPlusLeaseCondensateFetcher,
)
from .eia.crude_oil.imports import (
    CrudeOilImportsByCountryAndDestinationFetcher,
    CrudeOilImportsByCountryFetcher,
    CrudeOilImportsByDestinationFetcher,
    CrudeOilImportsByGradeFetcher,
)
from .eia.outlook.projections import IEOFetcher

provider = Provider(
    name="eia",
    description="U.S. Energy Information Administration provider for OpenBB Energy.",
    credentials=["api_key"],
    website="https://www.eia.gov/",
    fetcher_dict={
        "ConsumptionByEndUse": ConsumptionByEndUseFetcher,
        "ConsumptionNumberOfConsumers": ConsumptionNumberOfConsumersFetcher,
        "ConsumptionShareOfGasDelivered": ConsumptionShareOfGasDeliveredFetcher,
        "EnRCrudeOilPlusLeaseCondensate": EnRCrudeOilPlusLeaseCondensateFetcher,
        "ConsumptionAccountOfOthers": ConsumptionAccountOfOthersFetcher,
        "ConsumptionHeatContent": ConsumptionHeatContentFetcher,
        "CrudeOilImportsByCountryAndDestination": CrudeOilImportsByCountryAndDestinationFetcher,
        "CrudeOilImportsByCountry": CrudeOilImportsByCountryFetcher,
        "CrudeOilImportsByDestination": CrudeOilImportsByDestinationFetcher,
        "CrudeOilImportsByGrade": CrudeOilImportsByGradeFetcher,
        "InternationalEnergyOutlook": IEOFetcher,
    },
)
