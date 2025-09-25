from fastapi import APIRouter, Depends
from services.like_service import LikeService
from core.dependencies import get_like_service
from typing import List

router = APIRouter(prefix="/likes", tags=["likes"])


@router.post("/")
def add_like(user_id: int, blog_id: int, service: LikeService = Depends(get_like_service)):
    return service.add_like(user_id, blog_id)


@router.delete("/")
def remove_like(user_id: int, blog_id: int, service: LikeService = Depends(get_like_service)):
    return service.remove_like(user_id, blog_id)


@router.get("/blog/{blog_id}")
def get_likes_for_blog(blog_id: int, service: LikeService = Depends(get_like_service)):
    return service.get_likes_for_blog(blog_id)


@router.get("/user/{user_id}")
def get_likes_for_user(user_id: int, service: LikeService = Depends(get_like_service)):
    return service.get_likes_for_user(user_id)
