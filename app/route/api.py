from fastapi import APIRouter
from app.endpoint import user, status

router = APIRouter()
router.include_router(user.router)
router.include_router(status.router)
