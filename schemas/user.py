from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str


class BlogPreview(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True


class ProfilePreview(BaseModel):
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    profession: Optional[str] = None

    class Config:
        from_attributes = True



class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogPreview] = []
    profile: Optional[ProfilePreview] = None   

    class Config:
        from_attributes = True
