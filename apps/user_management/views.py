"""
This module contains the view functions for handling HTTP requests and rendering
responses for the application. It is responsible for processing user inputs,
interacting with the models, and returning the appropriate templates or JSON data.

"""

import logging
from fastapi import APIRouter, Depends, HTTPException
from .service import get_user_service
from sqlalchemy.orm import Session
from apps.user_management.repository.repository import ItemRepository
from apps.user_management.db_connection import get_db
from apps.user_management.models.models import Item
from apps.user_management.schemas.ItemSchema import ItemCreate, ItemRead

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
    except ValueError as e:
        logger.error(e)


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
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


@router.get("/db_item/{item_id}")
def read_item_name(item_id: int, db: Session = Depends(get_db)):
    logger.info("api service is started")
    db_item = ItemRepository.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.post("/items/", response_model=ItemRead)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = ItemRepository.create_item(db, item)
    return db_item
