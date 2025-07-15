from sqlalchemy import Column, Integer, String
from app.db.database import Base



class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(255), unique=True, index=True)
    price = Column(Integer)
    currency = Column(String(10))
    discount_rate = Column(Integer)
    stock = Column(Integer)
    slug = Column(String(255))
    attribute2_value = Column(String(255))
    attribute1_value = Column(String(255))
    attribute3_value = Column(String(255))
    attribute4_value = Column(String(255))
    product_type = Column(String(255))
    listing_type = Column(String(255))
    barcode = Column(String(255))
    sku = Column(String(255))
    shipping_charge = Column(Integer)
    status = Column(Integer)
    visibility = Column(Integer)


class Slider(Base):
    __tablename__ = 'slider'
    id = Column(Integer,primary_key=True, index=True)
    link = Column(String(255))
    image = Column(String(255))
 