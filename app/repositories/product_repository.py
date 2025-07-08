from sqlalchemy.orm import Session
from app.model.productModel import Product

def get_all_products(db:Session):
    return db.query(Product).all()