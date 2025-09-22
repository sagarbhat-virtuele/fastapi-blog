# routers/user.py
from fastapi import APIRouter, Depends, status
from schemas.user import User, ShowUser
from services.user_service import UserService
from core.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])  

@router.get("/{id}", response_model=ShowUser, status_code=status.HTTP_200_OK)
def get_user(id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(id)

@router.get("/", response_model=list[ShowUser], status_code=status.HTTP_200_OK)
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_all_users()

@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: User, service: UserService = Depends(get_user_service)):
    return service.create_user(request)

@router.put("/{id}", response_model=ShowUser, status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, request: User, service: UserService = Depends(get_user_service)):
    return service.update_user(id, request)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, service: UserService = Depends(get_user_service)):
    return service.delete_user(id)
