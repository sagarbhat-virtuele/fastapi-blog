from fastapi import FastAPI
from core.database import engine, Base
from routers import blog, user, profile
app = FastAPI()


# Base.metadata.drop_all(bind=engine) 
Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(profile.router)