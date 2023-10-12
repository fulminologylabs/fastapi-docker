import logging
from typing import List
from sqlalchemy.orm import Session
from app.database.connection import db_dep_injector
from app.schema import User, UserCreate, Item, ItemCreate
from app.database.operations.item import create_user_item
from app.database.operations.user import get_user_by_email, \
    create_user, get_users, get_user
from fastapi import Depends, HTTPException, status, APIRouter

logger = logging.getLogger("fastapi")
router = APIRouter()

@router.post("/create/", response_model=User)
def new_user(
    payload: UserCreate,
    session: Session = Depends(db_dep_injector),
):  
    try:
        db_user = get_user_by_email(session, payload.email)
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email is in use."
            )
        logger.info(f"Adding new user by: {payload.email}")
        return create_user(session, payload)
    except HTTPException as addressed_err:
        raise addressed_err
    except Exception as e:
        logger.exception(f"Failed to create new user with email: {payload.email}.")
        logger.exception(f"Error created user: {e}.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="failed to create user."
        )
    
@router.get("/view-all/", response_model=List[User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(db_dep_injector),
):
    try:
        users = get_users(skip=skip, limit=limit, session=session)
        return users
    except Exception as e:
        logger.exception(f"Failed to retrieve users with error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="failed to retrieve users."
        )
    
@router.get("/{user_id}", response_model=User)
def read_user(
    user_id: int,
    session: Session = Depends(db_dep_injector),
):
    try:
        db_user = get_user(session, user_id)
        if db_user is None:
            logger.error(f"Failed to find user with ID: {user_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found by this ID.")
    except HTTPException as addressed_err:
        raise addressed_err
    except Exception as e:
        err_msg = f"DB operation to find requested user could not be completed with error: {e}"
        logger.exception(err_msg)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=err_msg,
        )
    
@router.get("/{email}", response_model=User)
def read_user_by_email(
    email: str,
    session: Session = Depends(db_dep_injector),
):
    try:
        db_user = get_user_by_email(session, email)
        if db_user is None:
            logger.error(f"Failed to find user by requested email: {email}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="No user found by this email."
            )
    except HTTPException as addressed_err:
        raise addressed_err
    except Exception as e:
        err_msg = f"DB operation to find requested user could not be completed with error: {e}"
        logger.exception(err_msg)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=err_msg,
        )
    
@router.post("/{user_id}/item/create/", response_model=Item)
def add_item(
    user_id: int,
    item: ItemCreate,
    session: Session = Depends(db_dep_injector)
):
    # NOTE should have more fine-grained error handling
    try:
        user_item = create_user_item(session, item, user_id=user_id)
        return user_item
    except Exception as e:
        err_msg = f"Failed to add new {item.title} for user ID: {user_id} with error: {e}"
        logging.critical(err_msg)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=err_msg,
        )
