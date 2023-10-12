import logging
from app.config.config import config
from fastapi import APIRouter, HTTPException, status

router = APIRouter()
logger = logging.getLogger("fastapi")
# NOTE health-check does not relie on synchronous DB connection
@router.get("/health-check")
async def root():
    try:
        logger.info(f"Running {config.ENVIRONMENT}")
        return { "status": "healthy" }
    except Exception as e:
        logger.critical(f"health check failing with error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Cannot connect to API."
        )
    