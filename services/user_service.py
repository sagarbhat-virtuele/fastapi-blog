# services/user_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
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
            # raise HTTPException(
            #     status_code=status.HTTP_404_NOT_FOUND,
            #     detail=f"User with id {id} not found"
            # )
            return ResponseHandler.not_found(f"User with id {id} not found")
        return user
        # return ResponseHandler.ok(user, message="User fetched successfully")
        # return ResponseHandler.ok(data=ShowUser.model_validate(user))
    
    def get_all_users(self):
        return user_crud.get_users(self.db)

    def create_user(self, request: User):
        hashed_pass = pwd_context.hash(request.password)
        return user_crud.create_user(self.db, request, hashed_pass)

    def update_user(self, id: int, request: User):
        hashed_pass = pwd_context.hash(request.password)
        user = user_crud.update_user(self.db, id, request, hashed_pass)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {id} not found"
            )
        return user

    def delete_user(self, id: int):
        user = user_crud.delete_user(self.db, id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {id} not found"
            )
        return {"message": f"User with id {id} deleted"}
