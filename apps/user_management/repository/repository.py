from sqlalchemy.orm import Session
from apps.user_management.models.models import Item
from apps.user_management.schemas.ItemSchema import ItemCreate


class ItemRepository:

    @staticmethod
    def get_item(db: Session, item_id: int):
        return db.query(Item).filter(Item.id == item_id).first()

    @staticmethod
    def create_item(db: Session, item: ItemCreate):
        db_item = Item(name=item.name, description=item.description)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Item).offset(skip).limit(limit).all()
