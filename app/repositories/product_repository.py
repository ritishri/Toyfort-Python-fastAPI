from sqlalchemy.orm import Session
from sqlalchemy import text
from app.model.product_model import Product,Slider,ProductDetails,Category
import pandas as pd
from app.schemas.products_schema import AddCategories,ProductUpdate



def get_all_products(db:Session):
    return db.query(Product).all() 


def get_all_products_by_slug(db:Session, slug:str):
     query = text("SELECT  categories.*, products.*, product_details.*, images.*  from categories INNER JOIN products on categories.id = products.category_id INNER JOIN images ON images.product_id = products.id INNER JOIN product_details ON products.id = product_details.product_id where  categories.slug = :slug  AND images.is_main = 1 ORDER BY images.image_default DESC;")

     data = pd.read_sql_query(query, db.bind, params={"slug":slug})
     return data.to_dict(orient="records") 



def get_slider(db:Session):
     sliders =  db.query(Slider).all()
     return sliders


def get_brand_name(db:Session):
     query = text("SELECT DISTINCT attribute2_value FROM products WHERE attribute2_value IS NOT NULL ORDER BY attribute2_value ASC")

     data = pd.read_sql_query(query,db.bind)
     return data["attribute2_value"].tolist()


def create_product(db: Session, product_data: dict, product_details_data:dict ,user_id: int):
    product_data["user_id"] = user_id
    
    new_product = Product(**product_data)  
    db.add(new_product)
    db.commit()
    db.refresh(new_product) 
    new_product_id = new_product.id
    product_details_data["product_id"] = new_product_id
    new_product_details = ProductDetails(**product_details_data)
    db.add(new_product_details)
    db.commit()
    db.refresh(new_product_details)

    return {"details": new_product_details}


def update_product(db: Session, product_id: int, product_data: dict, details_data: dict):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None  

    for key, value in product_data.items():
        setattr(product, key, value)

    product_details = db.query(ProductDetails).filter(ProductDetails.product_id == product_id).first()
    if product_details:

        for key, value in details_data.items():
            setattr(product_details, key, value)

    db.commit()
    db.refresh(product)
    if product_details:
        db.refresh(product_details)

    return {"product": product, "details": product_details}




def add_category(db:Session, product_cat : AddCategories ):

    category = Category(**product_cat.dict())
    db.add(category)
    db.commit()
    db.refresh(category)

    return {"product": category}



# product.id == product_details.id, product_setails.product_id