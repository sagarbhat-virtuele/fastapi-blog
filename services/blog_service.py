# services/blog_service.py
from sqlalchemy.orm import Session
import crud.blog as blog_crud
from schemas.blog import Blog, ShowBlog
from utils.response_handler import ResponseHandler


class BlogService:
    def __init__(self, db: Session):
        self.db = db

    def get_blog(self, id: int):
        blog = blog_crud.get_blog(self.db, id)
        if not blog:
            return ResponseHandler.not_found(f"Blog with id {id} not found")

        return ResponseHandler.ok(
            data=ShowBlog.model_validate(blog).model_dump(),
            message="Blog fetched successfully"
        )

    def get_all_blogs(self):
        blogs = blog_crud.get_blogs(self.db)
        return ResponseHandler.ok(
            data=[ShowBlog.model_validate(b).model_dump() for b in blogs],
            message="All blogs fetched successfully"
        )

    def create_blog(self, request: Blog):
        blog = blog_crud.create_blog(self.db, request)
        return ResponseHandler.created(
            data=ShowBlog.model_validate(blog).model_dump(),
            message="Blog created successfully"
        )

    def update_blog(self, id: int, request: Blog):
        blog = blog_crud.update_blog(self.db, id, request)
        if not blog:
            return ResponseHandler.not_found(f"Blog with id {id} not found")

        return ResponseHandler.ok(
            data=ShowBlog.model_validate(blog).model_dump(),
            message="Blog updated successfully"
        )

    def delete_blog(self, id: int):
        blog = blog_crud.delete_blog(self.db, id)
        if not blog:
            return ResponseHandler.not_found(f"Blog with id {id} not found")

        return ResponseHandler.ok(
            message=f"Blog with id {id} deleted"
        )
