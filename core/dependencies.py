# dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services.blog_service import BlogService
from services.like_service import LikeService
from services.profile_service import ProfileService
from services.user_service import UserService
from services.auth_service import AuthService


def get_blog_service(db: Session = Depends(get_db)) -> BlogService:
    return BlogService(db)

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)

def get_profile_service(db=Depends(get_db)) -> ProfileService:
    return ProfileService(db)

def get_like_service(db: Session = Depends(get_db)) -> LikeService:  
    return LikeService(db)

def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)