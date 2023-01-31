from pydantic import BaseModel


class SecurityUser(BaseModel):
    role: str
