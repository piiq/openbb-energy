"""EIA Data Provider for OpenBB Energy."""
from openbb_core.provider.abstract.provider import Provider
from openbb_energy.eia.natural_gas.consumption_end_use import ConsumptionByEndUseFetcher
from openbb_energy.eia.natural_gas.consumption_number_of_consumers import (
    ConsumptionNumberOfConsumersFetcher,
)


# mypy: disable-error-code="list-item"

provider = Provider(
    name="eia",
    description="U.S. Energy Information Administration provider for OpenBB Energy.",
    credentials=["api_key"],
    website="https://www.eia.gov/",
    fetcher_dict={
        "ConsumptionByEndUse": ConsumptionByEndUseFetcher,
        "ConsumptionNumberOfConsumers": ConsumptionNumberOfConsumersFetcher,
    },
)
