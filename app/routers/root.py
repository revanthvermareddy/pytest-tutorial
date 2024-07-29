from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
def hello_world():
    return JSONResponse(content={"hello": "world"})

@router.get("/")
def health_check():
    return JSONResponse(content={"msg": "the app is up and running"})