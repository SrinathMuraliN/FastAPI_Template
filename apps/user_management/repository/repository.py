from sqlalchemy.orm import Session
from apps.user_management.models.models import Item
from apps.user_management.schemas.ItemSchema import UserCreate,Userupdate


class ItemRepository:

    @staticmethod
    def get_item(db: Session, item_id: int):
        return db.query(Item).filter(Item.id == item_id).first()

    @staticmethod
    def create_user(db: Session, item: UserCreate):
        db_item = Item(name=item.name, email_id=item.email_id, role = item.role)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Item).offset(skip).limit(limit).all()
    
    @staticmethod 
    def update_user(user_id: int, db: Session, upadte_user :Userupdate):
        db_user = db.query(Item).filter(Item.id == user_id).first()
        db_user.name = upadte_user.name
        db_user.email_id = upadte_user.email_id
        db_user.role = upadte_user.role
        db.commit()
        db.refresh(db_user)
        return db_user
    
    
    @staticmethod 
    def delete_user(user_id: int, db: Session):
        db.query(Item).filter(Item.id == user_id).delete()
        db.commit()
    
    
