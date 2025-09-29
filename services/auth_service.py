from sqlalchemy.orm import Session
import crud.authentication as auth_crud
from schemas.user import User, ShowUser
from schemas.authentication import UserLogin, Token
from utils.response_handler import ResponseHandler
from utils import security


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def login(self, request: UserLogin):
        user = auth_crud.get_user_by_email_or_name(self.db, request.username)
        if not user or not security.verify_password(request.password, user.password):
            return ResponseHandler.unauthorized("Invalid username/email or password")

        access_token = security.create_access_token(data={"sub": user.email})
        return ResponseHandler.ok(
            data=Token(access_token=access_token, token_type="bearer").model_dump(),
            message="Login successful"
        )

    def logout(self):
        return ResponseHandler.ok(message="Logout successful. Please discard the token on the client side.")

