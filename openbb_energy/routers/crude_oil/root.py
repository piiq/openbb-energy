"""Crude Oil router."""
from openbb_core.app.router import Router

from .imports import router as imports

router = Router(prefix="/crude_oil")
router.include_router(imports)