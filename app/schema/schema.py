from datetime import datetime
from pydantic import BaseModel

class ItemBase(BaseModel):
    """
        Used for create, base for others
    """
    title       : str 
    description : str


class ItemCreate(ItemBase):
    pass 


class Item(ItemBase):
    """
        Used for reading
    """
    id         : int 
    owner_id   : int
    created_at : datetime
    updated_at : datetime | None = None

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    """
        Used for create, base for others
    """
    email: str
    name : str | None = None


class UserCreate(UserBase):
    pass  


class User(UserBase):
    """
        Used for reading
    """
    id         : int
    created_at : datetime
    updated_at : datetime | None = None
    items      : list[Item] = []

    class Config:
        from_attributes = True