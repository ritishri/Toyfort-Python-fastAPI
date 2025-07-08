from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(255), unique=True, index=True)
    price = Column(Integer)
    currency = Column(String(10))
    discount_rate = Column(Integer)
    stock = Column(Integer)
