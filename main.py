from fastapi import FastAPI

from app.api.routes import router

app = FastAPI()

app.include_router(router, prefix="/api", tags=["api"])
# app.include_router(user_router, prefix="/api/stats", tags=["users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




