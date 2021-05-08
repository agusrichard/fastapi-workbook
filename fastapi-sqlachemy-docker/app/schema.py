from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    fullname: str = None

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True