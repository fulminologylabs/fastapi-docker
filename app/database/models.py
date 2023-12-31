from __future__ import annotations
from typing import List
from datetime import datetime
from sqlalchemy import ForeignKey, text
from sqlalchemy.types import JSON, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, \
    relationship

class Base(DeclarativeBase):
    type_annotations_map = {
        dict: JSON,
        datetime: DateTime,
    }


class Users(Base):
    __tablename__ = "users"
    id         : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email      : Mapped[str] = mapped_column(unique=True, nullable=False)
    name       : Mapped[str | None] = mapped_column(unique=True, index=True, nullable=True)
    created_at : Mapped[datetime] = mapped_column(index=True, server_default=text("statement_timestamp()"))
    updated_at : Mapped[datetime] = mapped_column(index=True, onupdate=text("statement_timestamp()"), nullable=True)
    # relationship
    items: Mapped[List[Item]] = relationship(back_populates="owner")


class Item(Base):
    __tablename__ = "item"
    id          : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title       : Mapped[str] = mapped_column(nullable=False)
    description : Mapped[str] = mapped_column(nullable=False)
    created_at : Mapped[datetime] = mapped_column(index=True, server_default=text("statement_timestamp()"))
    updated_at  : Mapped[datetime] = mapped_column(index=True, onupdate=text("statement_timestamp()"), nullable=True)
    # FK
    owner_id    : Mapped[int] = mapped_column(ForeignKey("users.id", onupdate="CASCADE", ondelete="RESTRICT"), index=True)
    # relationship
    owner       : Mapped[Users] = relationship(back_populates="items")

