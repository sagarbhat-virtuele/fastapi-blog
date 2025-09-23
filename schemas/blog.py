from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    user_id: int

# 👇 Minimal User schema to avoid circular imports
class UserPreview(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[UserPreview]

    class Config:
        from_attributes = True
