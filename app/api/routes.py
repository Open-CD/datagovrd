from fastapi import APIRouter

from app.controllers.sns_controller import router as sns_router

router = APIRouter()

#Here we add each enpoint  
router.include_router(sns_router, prefix="/sns", tags=["sns"])