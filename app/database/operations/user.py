from typing import List
from app.database import models
from sqlalchemy.orm import Session
from app.schema import User, UserCreate

def get_user(db: Session, user_id: int) -> User | None:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 1000) -> List[User]:
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate) -> User:
    db_user = models.User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
