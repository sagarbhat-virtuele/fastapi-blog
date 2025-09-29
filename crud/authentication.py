from sqlalchemy.orm import Session
from models.user import User
from schemas.authentication import UserLogin as UserSchema

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()

def get_user_by_email_or_name(db: Session, identifier: str):
    return db.query(User).filter(
        (User.email == identifier) | (User.name == identifier)
    ).first()

def create_user(db: Session, request: UserSchema, hashed_password: str):
    new_user = User(
        name=request.name,
        email=request.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user_password(db: Session, user_id: int, hashed_password: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.password = hashed_password
    db.commit()
    db.refresh(user)
    return user
