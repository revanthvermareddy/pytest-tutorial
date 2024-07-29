from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..config import settings


router = APIRouter()

@router.get("/info")
def get_info():
    response = {
        'app_name': settings.app_name,
        'admin_email': settings.admin_email
    }
    return JSONResponse(content=response)


