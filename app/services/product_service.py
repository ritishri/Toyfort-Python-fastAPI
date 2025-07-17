from app.repositories.product_repository import get_all_products,get_all_products_by_slug,get_slider,get_brand_name,create_product,update_product,add_category
from sqlalchemy.orm import Session
from app.schemas.products_schema import AddCategories,ProductCombinedCreate,ProductUpdate

def fetch_products(db:Session):
    return get_all_products(db)


def fetch_products_by_slug(db:Session, product_slug:str):
    return get_all_products_by_slug(db,product_slug)


def fetch_slider(db:Session):
    return get_slider(db)


def fetch_brand_name(db:Session):
    return get_brand_name(db)


def create_product_service(db: Session, combined_data: ProductCombinedCreate, user_id: int):
    data = combined_data.dict()

    product_keys = [
        "slug", "price", "currency", "discount_rate", "stock",
        "attribute2_value", "attribute2_name", "attribute1_name",
        "attribute1_value", "attribute3_name", "attribute3_value",
         "attribute4_name", "attribute4_value",
        "product_type", "listing_type", "barcode", "sku",
        "shipping_charge", "status", "visibility",
    ]
    product_data = {k: data[k] for k in product_keys}

    details_keys = [
        "title", "tag", "faqs", "description",
        "seo_title", "seo_description", "seo_keywords"
    ]
    details_data = {k: data[k] for k in details_keys}

    return create_product(db, product_data, details_data, user_id)



def update_product_service(db: Session, product_id: int, combined_data: ProductUpdate):
    data = combined_data.dict(exclude_unset=True)  

    product_keys = [
        "slug", "price", "currency", "discount_rate", "stock",
        "attribute2_value", "attribute2_name", "attribute1_name",
        "attribute1_value", "attribute3_name", "attribute3_value",
        "attribute4_name", "attribute4_value",
        "product_type", "listing_type", "barcode", "sku",
        "shipping_charge", "status", "visibility"
    ]
    details_keys = [
        "title", "tag", "faqs", "description",
        "seo_title", "seo_description", "seo_keywords"
    ]

    product_data = {k: data[k] for k in data if k in product_keys}
    details_data = {k: data[k] for k in data if k in details_keys}

    return update_product(db, product_id, product_data, details_data)




def add_category_service(product_cat: AddCategories, db:Session) :
    return  add_category(db,product_cat) 

