from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from utils.response_handler import ResponseHandler
import utils.security as security
from crud.authentication import get_user_by_email_or_name
from core.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = security.decode_access_token(token)
    if not token_data or not token_data.username:
        return ResponseHandler.unauthorized("Invalid or expired token")

    user = get_user_by_email_or_name(db, token_data.username)
    if not user:
        return ResponseHandler.unauthorized("User not found")

    return user
