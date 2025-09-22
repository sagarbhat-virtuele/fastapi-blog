# routers/blog.py
from fastapi import APIRouter, Depends, status
from schemas.blog import Blog, ShowBlog
from services.blog_service import BlogService
from core.dependencies import get_blog_service

router = APIRouter(prefix="/blogs", tags=["blogs"])

@router.get("/{id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
def read_blog(id: int, service: BlogService = Depends(get_blog_service)):
    return service.get_blog(id)

@router.get("/", response_model=list[ShowBlog], status_code=status.HTTP_200_OK)
def get_blogs(service: BlogService = Depends(get_blog_service)):
    return service.get_all_blogs()

@router.post("/", status_code=status.HTTP_201_CREATED)
def post_blogs(request: Blog, service: BlogService = Depends(get_blog_service)):
    return service.create_blog(request)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: Blog, service: BlogService = Depends(get_blog_service)):
    return service.update_blog(id, request)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, service: BlogService = Depends(get_blog_service)):
    return service.delete_blog(id)
