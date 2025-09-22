# services/blog_service.py
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import crud.blog as blog_crud
from schemas.blog import Blog, ShowBlog
class BlogService:
    def __init__(self, db: Session):
        self.db = db

    def get_blog(self, id: int):
        blog = blog_crud.get_blog(self.db, id)
        if not blog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with id {id} not found"
            )
        return blog

    def get_all_blogs(self):
        return blog_crud.get_blogs(self.db)

    def create_blog(self, request: Blog):
        return blog_crud.create_blog(self.db, request)

    def update_blog(self, id: int, request: Blog):
        blog = blog_crud.update_blog(self.db, id, request)
        if not blog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with id {id} not found"
            )
        return blog

    def delete_blog(self, id: int):
        blog = blog_crud.delete_blog(self.db, id)
        if not blog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with id {id} not found"
            )
        return {"message": f"Blog with id {id} deleted"}
