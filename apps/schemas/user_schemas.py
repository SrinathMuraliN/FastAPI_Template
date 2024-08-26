from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email_id: str
    role : str
    
class UserUpdate(BaseModel):
    name:Optional[str] = None
    email_id:Optional[str] = None
    role :Optional[str] =None


class UserRead(UserCreate):
    id: int

    class Config:
        orm_mode = True
