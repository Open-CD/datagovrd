from fastapi import FastAPI

from app.api.routes import router

app = FastAPI()

app.include_router(router, prefix="/api", tags=["api"])
# app.include_router(user_router, prefix="/api/stats", tags=["users"])
