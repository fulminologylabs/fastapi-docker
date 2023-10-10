import logging
from app.config.config import config
from fastapi import APIRouter, HTTPException


router = APIRouter()
logger = logging.getLogger("fastapi")

@router.get("/health-check")
async def root():
    try:
        logger.info(f"Running {config.ENVIRONMENT}")
        return { "status": "healthy" }
    except Exception as e:
        logger.critical(f"health check failing with error: {e}")
        raise HTTPException(status_code=500, detail="Cannot connect to API.")
    