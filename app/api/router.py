from fastapi import APIRouter
from app.utils.constants import API_PREFIX
from app.api.endpoints import (
    user,
    item,
    health_check,
)

router = APIRouter(prefix=API_PREFIX)

router.include_router(user.router, prefix="/user", tags=["user"])
router.include_router(item.router, prefix="/item", tags=["item"])
router.include_router(health_check.router, tags=["health"])
