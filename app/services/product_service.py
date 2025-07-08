from app.repositories.product_repository import get_all_products
from sqlalchemy.orm import Session

def fetch_products(db:Session):
    return get_all_products(db)