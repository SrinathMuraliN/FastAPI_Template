"""
This module contains the view functions for handling HTTP requests and rendering
responses for the application. It is responsible for processing user inputs,
interacting with the models, and returning the appropriate templates or JSON data.

"""

import logging

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi_cache.decorator import cache

from apps.services.user_management_service import get_user_service

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/get_user")
@cache(namespace="login", expire=60)
async def get_users(authorization: str = Depends(HTTPBearer)):
    """
    Function to fetch user list
    """
    try:
        logger.info("Start of the view")
        user_lsit = get_user_service()
        logger.info("End of the view")
        return user_lsit
    except ValueError as e:
        logger.error(e)


@router.get("/items/{item_id}")
@cache(namespace="login", expire=60)
def read_item(item_id: int, q: str = None, authorization: str = Depends(HTTPBearer)):
    """
    Retrieve an item by ID. If there is no optional
    String Provided, In the return dict, It retruns the value as None

    Args:
        item_id (int): The ID of the item.
        q (str, optional): An optional query string.

    Returns:
        dict: A dictionary containing the item's details like item id
            & the optinal string
    Raises:
        HTTPException: If the item_id is invalid.
        ValueError: If the `id` provided is not a positive integer.
    """
    logger.info("Start of the view")
    if item_id == 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    logger.info("End of the view")
    return {"item_id": item_id, "q": q}
