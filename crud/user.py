# crud/user.py
from sqlalchemy.orm import Session
from schemas.user import User, ShowUser
from models.user import User

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, request: User, hashed_password: str):
    new_user = User(
        name=request.name,
        email=request.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user_id: int, request: User, hashed_password: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.name = request.name
    user.email = request.email
    user.password = hashed_password
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user
