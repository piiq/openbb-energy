"""Natural Gas router."""
from openbb_core.app.router import Router
from .consumption import router as consumption
from .exploration_and_reserves import router as exploration_and_reserves
from .imports_and_exports import router as imports_and_exports
from .production import router as production
from .storage import router as storage

router = Router(prefix="/natural_gas")
router.include_router(consumption)
router.include_router(exploration_and_reserves)
router.include_router(imports_and_exports)
router.include_router(production)
router.include_router(storage)
