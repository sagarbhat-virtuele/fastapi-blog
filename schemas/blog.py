from typing import Optional
from pydantic import BaseModel
from schemas.user import ShowUser


class Blog(BaseModel):
    title: str
    body: str
    user_id: int


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUser]
    class Config():
        orm_mode = True