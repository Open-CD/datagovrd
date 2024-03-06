from fastapi import FastAPI
import uvicorn

from app.api.routes import router

app = FastAPI()

app.include_router(router, prefix="/api", tags=["api"])

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

