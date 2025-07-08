from app.repositories.product_repository import get_all_products,get_all_products_by_slug
from sqlalchemy.orm import Session


def fetch_products(db:Session):
    return get_all_products(db)


def fetch_products_by_slug(db:Session, product_slug:str):
    return get_all_products_by_slug(db,product_slug)