"""OpenBB Energy router."""

from openbb_core.app.router import Router
from .routers.natural_gas.root import router as natural_gas
from .routers.outlook.projections import router as ieo


router = Router(prefix="")
router.include_router(natural_gas)
router.include_router(ieo)
