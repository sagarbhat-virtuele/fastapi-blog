# routers/blog.py
from fastapi import APIRouter, Depends
from schemas.blog import Blog
from services.blog_service import BlogService
from core.dependencies import get_blog_service

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get("/{id}")
def read_blog(id: int, service: BlogService = Depends(get_blog_service)):
    return service.get_blog(id)


@router.get("/")
def get_blogs(service: BlogService = Depends(get_blog_service)):
    return service.get_all_blogs()


@router.post("/")
def post_blogs(request: Blog, service: BlogService = Depends(get_blog_service)):
    return service.create_blog(request)


@router.put("/{id}")
def update_blog(id: int, request: Blog, service: BlogService = Depends(get_blog_service)):
    return service.update_blog(id, request)


@router.delete("/{id}")
def delete_blog(id: int, service: BlogService = Depends(get_blog_service)):
    return service.delete_blog(id)
