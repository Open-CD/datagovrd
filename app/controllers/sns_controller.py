from fastapi import APIRouter

from app.services.sns_service import GeneralService, StatsService

router = APIRouter()

@router.get("/")
def get_general():
    return {
        "title": "Servicio Nacional de Salud",
        "abbreviation": "SNS",
        "description": GeneralService.get_about()
    }

@router.get("/stats/info")
def get_stats_info():
    return {
        "title": StatsService.get_title(),
        "available_years": StatsService.get_available_years()
    }