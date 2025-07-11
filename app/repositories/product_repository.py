from sqlalchemy.orm import Session
from sqlalchemy import text
from app.model.product_model import Product,Slider
import pandas as pd



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
      