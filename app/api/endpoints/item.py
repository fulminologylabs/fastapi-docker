import logging
from typing import List
from app.schema.schema import Item
from sqlalchemy.orm import Session
from app.database.connection import db_dep_injector
from fastapi import Depends, HTTPException, status, APIRouter
from app.database.operations.item import get_items_by_user, get_items

logger = logging.getLogger("fastapi")
router = APIRouter()

@router.get("/{user_id}", response_model=List[Item])
def read_items_by_user(
    user_id: int,
    session: Session = Depends(db_dep_injector),
):
    try:
        user_items = get_items_by_user(user_id=user_id, db=session)
        return user_items
    except Exception as e:
        err_msg = f"Failed to retreive user items for user: {user_id} with error: {e}."
        logging.critical(err_msg)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=err_msg,
        )
    
@router.get("/all/", response_model=List[Item])
def read_all_items(
    session: Session = Depends(db_dep_injector),
):
    try:
        items = get_items(session)
        return items
    except Exception as e:
        err_msg = f"Failed to retrieve items with error: {e}."
        logging.critical(err_msg)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=err_msg,
        )