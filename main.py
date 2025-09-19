from fastapi import FastAPI, Depends, HTTPException, status
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import schema

app = FastAPI()


# models.Base.metadata.drop_all(bind=engine) 
models.Base.metadata.create_all(engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schema.ShowBlog, tags=['blog'])
def read_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog

@app.get("/blogs", status_code=status.HTTP_200_OK, response_model=list[schema.ShowBlog], tags=['blog'])
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.post("/blog", status_code=status.HTTP_201_CREATED, tags=['blog'])
def post_blogs(request: schema.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['blog'])
def update_blog(id: int, request: schema.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    blog.title = request.title
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return blog

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=['blog'])
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    db.delete(blog)
    db.commit()
    return {"message": f"Blog with id {id} deleted"}

@app.post("/user", response_model=schema.ShowUser, status_code=status.HTTP_201_CREATED, tags=['user'])
def create_user(request: schema.User, db: Session = Depends(get_db)):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_pass = pwd_context.hash(request.password)
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hashed_pass
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/user/{id}", response_model=schema.ShowUser, status_code=status.HTTP_200_OK, tags=['user'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    return user