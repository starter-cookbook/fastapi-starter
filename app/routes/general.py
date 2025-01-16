from fastapi import APIRouter
from app.config import CONFIG_CHECK

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "general route"}

@router.get("/config-check")
async def config_check():
    return {"value": CONFIG_CHECK }