import logging
from typing import List

from fastapi import Depends, HTTPException, status

from app.model.security_user import SecurityUser
from app.security.security_config import get_current_active_user


class RoleChecker:
    """constructor => roleChecker = RoleChecker([])"""
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    # call created object => roleChecker()
    def __call__(self, user: SecurityUser = Depends(get_current_active_user)):
        if user.role not in self.allowed_roles:
            logging.debug(f"User with role {user.role} not in {self.allowed_roles}")
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation not permitted")
