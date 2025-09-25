from pydantic import BaseModel

class UserPreview(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class BlogPreview(BaseModel):
    id: int
    title: str
    body: str

    class Config:
        from_attributes = True


class ShowLike(BaseModel):
    id: int
    user: UserPreview
    blog: BlogPreview

    class Config:
        from_attributes = True
