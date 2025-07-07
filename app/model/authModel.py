from sqlalchemy import Column,Integer,String
from app.db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String(255), unique=True, index=True)
    first_name = Column(String(255),nullable=False)
    last_name = Column(String(255),nullable=False)
    phone_number = Column(String(10),nullable=False)
    password = Column(String(255),nullable=False)
    
    