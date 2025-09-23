# routers/user.py
from fastapi import APIRouter, Depends
from schemas.user import User
from services.user_service import UserService
from core.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])  


@router.get("/{id}")
def get_user(id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(id)


@router.get("/")
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_all_users()


@router.post("/")
def create_user(request: User, service: UserService = Depends(get_user_service)):
    return service.create_user(request)


@router.put("/{id}")
def update_user(id: int, request: User, service: UserService = Depends(get_user_service)):
    return service.update_user(id, request)


@router.delete("/{id}")
def delete_user(id: int, service: UserService = Depends(get_user_service)):
    return service.delete_user(id)
