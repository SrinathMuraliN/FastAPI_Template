from sqlalchemy import Column, Integer, String
from utility.db_connection import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email_id = Column(String, index=True)
    role = Column(String,index = True)