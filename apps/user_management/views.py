import logging
from fastapi import APIRouter
from .service import get_user_service

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/get_user")
async def get_users():
    """
    Function to fetch user list
    """
    try:
        logger.info("Start of the view")
        user_lsit = get_user_service()
        logger.info("End of the view")
        return user_lsit
    except Exception as e:
        logger.error(e)

