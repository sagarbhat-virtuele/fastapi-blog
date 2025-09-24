# dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services.blog_service import BlogService
from services.profile_service import ProfileService
from services.user_service import UserService

def get_blog_service(db: Session = Depends(get_db)) -> BlogService:
    return BlogService(db)

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)

def get_profile_service(db=Depends(get_db)):
    return ProfileService(db)