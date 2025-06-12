from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    email: str
    is_active: bool = True

class UserOut(UserIn):
    id: int
