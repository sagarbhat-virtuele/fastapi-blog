from sqlalchemy.orm import Session
from models.profile import Profile
from schemas.profile import Profile as ProfileSchema


def get_profile(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()


def get_profile_by_user(db: Session, user_id: int):
    return db.query(Profile).filter(Profile.user_id == user_id).first()


def create_profile(db: Session, request: ProfileSchema):
    new_profile = Profile(
        bio=request.bio,
        avatar_url=request.avatar_url,
        profession=request.profession,
        user_id=request.user_id
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile


def update_profile(db: Session, profile_id: int, request: ProfileSchema):
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if not profile:
        return None
    profile.bio = request.bio
    profile.avatar_url = request.avatar_url
    profile.profession = request.profession
    db.commit()
    db.refresh(profile)
    return profile


def delete_profile(db: Session, profile_id: int):
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if not profile:
        return None
    db.delete(profile)
    db.commit()
    return profile
