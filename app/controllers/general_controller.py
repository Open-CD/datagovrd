from fastapi import APIRouter

from app.utils.data import institutions_arr

router = APIRouter()

@router.get("/")
def get_general():
    return {
        "institutions": institutions_arr
    }