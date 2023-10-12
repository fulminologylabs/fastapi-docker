from typing import List
from app.database import models
from sqlalchemy.orm import Session
from app.schema import ItemCreate, Item

def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_items_by_user(db: Session, user_id: int) -> List[Item]:
    return db.query(models.Item).filter(models.Item.owner_id == user_id).all()

def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = models.Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
