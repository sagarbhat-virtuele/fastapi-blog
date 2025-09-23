from typing import List
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

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogPreview] = []

    class Config:
        from_attributes = True
