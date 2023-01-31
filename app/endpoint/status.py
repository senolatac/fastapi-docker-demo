import logging

from fastapi import APIRouter, Depends

# APIRouter creates path operations for user module
from app.security.role_checker import RoleChecker
from app.security.security_config import USER

router = APIRouter(
    prefix="/health",
    tags=["Status"],
    responses={404: {"description": "Not found"}},
)

allow_create_resource = RoleChecker([USER])


@router.get("/check")
async def get_status():
    logging.info("Get status requested")
    return {"status": "UP"}


@router.get("/check-with-auth", dependencies=[Depends(allow_create_resource)])
async def get_status_with_auth():
    logging.info("Get status requested with auth header")
    return {"status": "UP"}
