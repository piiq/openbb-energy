"""Natural Gas router."""
from openbb_core.app.router import Router
from .consumption import router as consumption

router = Router(prefix="/natural_gas")
router.include_router(consumption)
