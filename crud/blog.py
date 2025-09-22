from sqlalchemy.orm import Session
from schemas.blog import Blog, ShowBlog
from models.blog import Blog

def get_blog(db: Session, blog_id: int):
    return db.query(Blog).filter(Blog.id == blog_id).first()

def get_blogs(db: Session):
    return db.query(Blog).all()

def create_blog(db: Session, request: Blog):
    new_blog = Blog(title=request.title, body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update_blog(db: Session, blog_id: int, request: Blog):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        return None
    blog.title = request.title
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return blog

def delete_blog(db: Session, blog_id: int):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        return None
    db.delete(blog)
    db.commit()
    return blog
