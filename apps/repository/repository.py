from sqlalchemy.orm import Session
from apps.models.user_models import User
from apps.serializer.serializer import UserCreate, UserUpdate


class UserRepository:

    @staticmethod
    def get_item(db: Session, item_id: int):
        return db.query(User).filter(User.id == item_id).first()
    
    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 10):
        return db.query(User).offset(skip).limit(limit).all()



    @staticmethod
    def create_user(db: Session, item: UserCreate):
        print(item)
        db_item = User(name=item.name, email_id=item.email_id, role = item.role)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 10):
        return db.query(User).offset(skip).limit(limit).all()
    
    @staticmethod 
    def update_user(user_id: int, db: Session, upadte_user:UserUpdate):
        db_user = db.query(User).filter(User.id == user_id).first()
        db_user.name = upadte_user.name
        db_user.email_id = upadte_user.email_id
        db_user.role = upadte_user.role
        db.commit()
        db.refresh(db_user)
        return db_user
    
    
    @staticmethod 
    def delete_user(user_id: int, db: Session):
        db.query(User).filter(User.id == user_id).delete()
        db.commit()
    
    

    
   