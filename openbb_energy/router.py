"""OpenBB Energy router."""

from openbb_core.app.router import Router
from .routers.natural_gas.root import router as natural_gas


router = Router(prefix="")
router.include_router(natural_gas)
