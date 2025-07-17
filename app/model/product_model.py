from sqlalchemy import Column, Integer, String
from app.db.database import Base



class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
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
    attribute2_name = Column(String(255))
    attribute1_name = Column(String(255))
    attribute3_name = Column(String(255))
    attribute4_name = Column(String(255))
    product_type = Column(String(255))
    listing_type = Column(String(255))
    barcode = Column(String(255))
    sku = Column(String(255))
    shipping_charge = Column(Integer)
    status = Column(Integer)
    visibility = Column(Integer)
    # product_type = Column(String(255))
    # faqs = Column(String(255))
    # description = Column(String(255))
    # tags = Column(String(255))
    # stock = Column(Integer)
    # barcode = Column(String(255))


class ProductDetails(Base):
    __tablename__ = "product_details"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer,nullable=False)

    title = Column(String(255))
    tag = Column(String(255))
    faqs = Column(String(255))
    description = Column(String(1000))
    seo_title = Column(String(255))
    seo_description = Column(String(500))
    seo_keywords = Column(String(500))




class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(255))
    title_meta_tag = Column(String(255))
    description = Column(String(255))
    keywords = Column(String(255))
    category_order = Column(String(255))
    visibility = Column(Integer)
    show_on_main_menu = Column(Integer)
    show_image_on_main_menu = Column(Integer)
    # image = Column(String(255))




class Slider(Base):
    __tablename__ = 'slider'
    id = Column(Integer,primary_key=True, index=True)
    link = Column(String(255))
    image = Column(String(255))
 