from sqlalchemy.orm import Session
from schemas.profile import Profile, ShowProfile
import crud.profile as profile_crud
from utils.response_handler import ResponseHandler


class ProfileService:
    def __init__(self, db: Session):
        self.db = db

    def get_profile(self, profile_id: int):
        profile = profile_crud.get_profile(self.db, profile_id)
        if not profile:
            return ResponseHandler.not_found(f"Profile with id {profile_id} not found")
        return ResponseHandler.ok(
            data=ShowProfile.model_validate(profile).model_dump(),
            message="Profile fetched successfully"
        )

    def get_profile_by_user(self, user_id: int):
        profile = profile_crud.get_profile_by_user(self.db, user_id)
        if not profile:
            return ResponseHandler.not_found(f"Profile for user {user_id} not found")
        return ResponseHandler.ok(
            data=ShowProfile.model_validate(profile).model_dump(),
            message="Profile fetched successfully"
        )

    def create_profile(self, request: Profile):
        profile = profile_crud.create_profile(self.db, request)
        return ResponseHandler.created(
            data=ShowProfile.model_validate(profile).model_dump(),
            message="Profile created successfully"
        )

    def update_profile(self, profile_id: int, request: Profile):
        profile = profile_crud.update_profile(self.db, profile_id, request)
        if not profile:
            return ResponseHandler.not_found(f"Profile with id {profile_id} not found")
        return ResponseHandler.ok(
            data=ShowProfile.model_validate(profile).model_dump(),
            message="Profile updated successfully"
        )

    def delete_profile(self, profile_id: int):
        profile = profile_crud.delete_profile(self.db, profile_id)
        if not profile:
            return ResponseHandler.not_found(f"Profile with id {profile_id} not found")
        return ResponseHandler.ok(
            message=f"Profile with id {profile_id} deleted"
        )
