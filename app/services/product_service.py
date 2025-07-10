from app.repositories.product_repository import get_all_products,get_all_products_by_slug,get_slider,get_brand_name
from sqlalchemy.orm import Session


def fetch_products(db:Session):
    return get_all_products(db)


def fetch_products_by_slug(db:Session, product_slug:str):
    return get_all_products_by_slug(db,product_slug)


def fetch_slider(db:Session):
    return get_slider(db)


def fetch_brand_name(db:Session):
    return get_brand_name(db)