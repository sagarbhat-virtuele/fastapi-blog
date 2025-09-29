from fastapi import APIRouter, Depends
from schemas.user import User, ShowUser
from schemas.authentication import UserLogin, Token
from services.auth_service import AuthService
from core.dependencies import get_auth_service

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login", response_model=Token)
def login(request: UserLogin, service: AuthService = Depends(get_auth_service)):
    return service.login(request)


@router.post("/logout")
def logout(service: AuthService = Depends(get_auth_service)):
    return service.logout()


