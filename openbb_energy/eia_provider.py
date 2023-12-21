"""EIA Data Provider for OpenBB Energy."""
from openbb_core.provider.abstract.provider import Provider

from openbb_energy.eia.natural_gas.consumption import (
    ConsumptionByEndUseFetcher,
    ConsumptionNumberOfConsumersFetcher,
    ConsumptionShareOfGasDeliveredFetcher,
)
from openbb_energy.eia.natural_gas.exploration_and_reserves import (
    EnRCrudeOilPlusLeaseCondensateFetcher,
)

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
    },
)
