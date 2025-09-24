from fastapi import APIRouter, Depends
from schemas.profile import Profile
from services.profile_service import ProfileService
from core.dependencies import get_profile_service

router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/{id}")
def get_profile(id: int, service: ProfileService = Depends(get_profile_service)):
    return service.get_profile(id)


@router.get("/user/{user_id}")
def get_profile_by_user(user_id: int, service: ProfileService = Depends(get_profile_service)):
    return service.get_profile_by_user(user_id)


@router.post("/")
def create_profile(request: Profile, service: ProfileService = Depends(get_profile_service)):
    return service.create_profile(request)


@router.put("/{id}")
def update_profile(id: int, request: Profile, service: ProfileService = Depends(get_profile_service)):
    return service.update_profile(id, request)


@router.delete("/{id}")
def delete_profile(id: int, service: ProfileService = Depends(get_profile_service)):
    return service.delete_profile(id)
