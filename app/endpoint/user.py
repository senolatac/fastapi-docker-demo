import logging

from fastapi import APIRouter, Depends
from fastapi import Query

from typing import Optional

# APIRouter creates path operations for user module
from app.security.role_checker import RoleChecker
from app.security.security_config import USER

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

allow_create_resource = RoleChecker([USER])


@router.get("/")
async def read_root():
    return [{"id": 1}, {"id": 2}]


@router.get("/dummy/{user_id}", dependencies=[Depends(allow_create_resource)])
async def read_user(user_id: int):
    logging.info("Read user request with %s", user_id)
    return {"id": user_id, "full_name": "Danny Manny", "email": "danny.manny@gmail.com"}


@router.get("/detail")
async def read_users(q: Optional[str] = Query(None, max_length=50)):
    results = {"users": [{"id": 1}, {"id": 2}]}
    if q:
        results.update({"q": q})
    return results
