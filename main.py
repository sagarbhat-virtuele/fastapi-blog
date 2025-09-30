from fastapi import FastAPI
from core.database import engine, Base
from routers import blog, user, profile, like, authentication
from fastapi.middleware.cors import CORSMiddleware
from core.auth_dependencies import get_current_user
from fastapi import Depends

app = FastAPI()

Base.metadata.create_all(engine)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(profile.router)
app.include_router(like.router)
app.include_router(authentication.router)

# app.include_router(blog.router, dependencies=[Depends(get_current_user)])
# app.include_router(user.router, dependencies=[Depends(get_current_user)])
# app.include_router(profile.router, dependencies=[Depends(get_current_user)])
# app.include_router(like.router, dependencies=[Depends(get_current_user)])
# app.include_router(authentication.router)
