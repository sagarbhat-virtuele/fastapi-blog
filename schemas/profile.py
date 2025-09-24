from pydantic import BaseModel
from typing import Optional


class Profile(BaseModel):
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    profession: Optional[str] = None
    user_id: int   


class UserPreview(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class ShowProfile(BaseModel):
    id: int
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    profession: Optional[str] = None
    user_id: int
    user: Optional[UserPreview] = None   

    class Config:
        from_attributes = True

