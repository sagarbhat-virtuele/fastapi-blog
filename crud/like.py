from sqlalchemy.orm import Session
from models.like import Like

def add_like(db: Session, user_id: int, blog_id: int):
    # Check if the like already exists
    existing = db.query(Like).filter(Like.user_id == user_id, Like.blog_id == blog_id).first()
    if existing:
        return None  # Already liked

    like = Like(user_id=user_id, blog_id=blog_id)
    db.add(like)
    db.commit()
    db.refresh(like)
    return like

def remove_like(db: Session, user_id: int, blog_id: int):
    like = db.query(Like).filter(Like.user_id == user_id, Like.blog_id == blog_id).first()
    if not like:
        return None
    db.delete(like)
    db.commit()
    return like

def get_likes_for_blog(db: Session, blog_id: int):
    return db.query(Like).filter(Like.blog_id == blog_id).all()

def get_likes_for_user(db: Session, user_id: int):
    return db.query(Like).filter(Like.user_id == user_id).all()
