from pydantic import BaseModel
from typing import Optional


class UserModel(BaseModel):
    user_id: Optional[int] = None
    username: str
    email: str
    password: str
