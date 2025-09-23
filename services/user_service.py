# services/user_service.py
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from schemas.user import User, ShowUser
import crud.user as user_crud
from utils.response_handler import ResponseHandler


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, id: int):
        user = user_crud.get_user(self.db, id)
        if not user:
            return ResponseHandler.not_found(f"User with id {id} not found")

        return ResponseHandler.ok(
            data=ShowUser.model_validate(user).model_dump(),
            message="User fetched successfully"
        )

    def get_all_users(self):
        users = user_crud.get_users(self.db)
        return ResponseHandler.ok(
            data=[ShowUser.model_validate(u).model_dump() for u in users],
            message="All users fetched successfully"
        )

    def create_user(self, request: User):
        hashed_pass = pwd_context.hash(request.password)
        user = user_crud.create_user(self.db, request, hashed_pass)
        return ResponseHandler.created(
            data=ShowUser.model_validate(user).model_dump(),
            message="User created successfully"
        )

    def update_user(self, id: int, request: User):
        hashed_pass = pwd_context.hash(request.password)
        user = user_crud.update_user(self.db, id, request, hashed_pass)
        if not user:
            return ResponseHandler.not_found(f"User with id {id} not found")

        return ResponseHandler.ok(
            data=ShowUser.model_validate(user).model_dump(),
            message="User updated successfully"
        )

    def delete_user(self, id: int):
        user = user_crud.delete_user(self.db, id)
        if not user:
            return ResponseHandler.not_found(f"User with id {id} not found")

        return ResponseHandler.ok(
            message=f"User with id {id} deleted"
        )
