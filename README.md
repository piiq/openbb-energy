# Energy Analysis Data and Tools for OpenBB

## Usage

```python
from openbb import obb
help(obb.eia.natural_gas.exploration_and_reserves.crude_plus_lease)
```

## Install for development

1. Clone the repository
2. Checkout the `develop` branch
3. Create and activate new virtual environment
   1. `python3 -m virtualenv venv`
   2. `source venv/bin/activate`
4. Install dependencies
   1. `pip install poetry`
5. Install package in editable mode
   1. `poetry install`
6. Install openbb without dependencies
   1. `pip install openbb --no-deps`

### Force rebuild the package

`python -c "import openbb; openbb.build()"`
