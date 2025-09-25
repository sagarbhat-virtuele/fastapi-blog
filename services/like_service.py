from sqlalchemy.orm import Session
import crud.like as like_crud
from schemas.like import ShowLike
from utils.response_handler import ResponseHandler

class LikeService:
    def __init__(self, db: Session):
        self.db = db

    def add_like(self, user_id: int, blog_id: int):
        like = like_crud.add_like(self.db, user_id, blog_id)
        if not like:
            return ResponseHandler.bad_request("User already liked this blog")
        return ResponseHandler.ok(
            data=ShowLike.model_validate(like).model_dump(),
            message="Blog liked successfully"
        )

    def remove_like(self, user_id: int, blog_id: int):
        like = like_crud.remove_like(self.db, user_id, blog_id)
        if not like:
            return ResponseHandler.not_found("Like not found")
        return ResponseHandler.ok(
            message="Like removed successfully"
        )

    def get_likes_for_blog(self, blog_id: int):
        likes = like_crud.get_likes_for_blog(self.db, blog_id)
        return ResponseHandler.ok(
            data=[ShowLike.model_validate(l).model_dump() for l in likes],
            message=f"All likes for blog {blog_id}"
        )

    def get_likes_for_user(self, user_id: int):
        likes = like_crud.get_likes_for_user(self.db, user_id)
        return ResponseHandler.ok(
            data=[ShowLike.model_validate(l).model_dump() for l in likes],
            message=f"All likes by user {user_id}"
        )
