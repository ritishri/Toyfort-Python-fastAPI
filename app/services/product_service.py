from app.repositories.product_repository import get_all_products,get_all_products_by_slug,get_slider,get_brand_name,create_product,update_product
from sqlalchemy.orm import Session


def fetch_products(db:Session):
    return get_all_products(db)


def fetch_products_by_slug(db:Session, product_slug:str):
    return get_all_products_by_slug(db,product_slug)


def fetch_slider(db:Session):
    return get_slider(db)


def fetch_brand_name(db:Session):
    return get_brand_name(db)



def create_product_service(db, product, user_id):
    return create_product(db, product.dict(), user_id)


def update_product_service(db, product_id, user_id, update_data):
    return update_product(db, product_id, user_id, update_data)

