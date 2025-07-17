from pydantic import BaseModel
from typing import Optional

class ProductResponse(BaseModel):
    id : int
    slug : str
    price : int
    currency : str
    discount_rate : int
    stock : int 
    slug : str  
    attribute2_value : str 
    # attribute2_name : str
    # attribute1_name : str
    # attribute1_value : str
    # attribute3_name : str
    # attribute3_value : str
    # product_type: str
    # listing_type: str
    # barcode: str
    # sku: str
    # shipping_charge: int
    # status: int
    # visibility: int
    class Config:
        orm_mode = True


class ProductResponseBySlug(BaseModel):
    id : int
    slug : str
    price : int
    currency : str
    discount_rate : int
    stock : int 
    slug : str
    image : str
    image_default : str
    description :str
    price : int


    class Config:
        orm_code = True

class sliderResponse(BaseModel):
    id : int
    link : Optional[str]  
    image : Optional[str]     

    class Config:
        orm_code = True

class ProductCreate(BaseModel):
    slug : str
    price : int
    currency : str
    discount_rate : int
    stock : int 
    slug : str  
    attribute2_value : str 
    attribute2_name : str
    attribute1_name : str
    attribute1_value : str
    attribute3_name : str
    attribute3_value : str
    attribute4_name: str
    attribute4_value: str
    product_type: str
    listing_type: str
    barcode: str
    sku: str
    shipping_charge: int
    status: int
    visibility: int
    product_type: str
    categories:str
    stock : str
    barcode : str
    class Config:
        orm_mode = True
       


class ProductUpdate(BaseModel):
     slug: Optional[str] = None
     price: Optional[int] = None
     currency: Optional[str] = None
     discount_rate: Optional[int] = None
     stock: Optional[int] = None
     attribute1_value: Optional[str] = None
     attribute2_value: Optional[str] = None
     attribute3_value: Optional[str] = None
     attribute4_value: Optional[str] = None
     product_type: Optional[str] = None
     listing_type: Optional[str] = None
     barcode: Optional[str] = None
     sku: Optional[str] = None
     shipping_charge: Optional[int] = None
     status: Optional[int] = None
     visibility: Optional[int] = None
     faqs: Optional[str] = None
     description: Optional[str] = None
     tags: Optional[str] = None
    


     class Config:
        orm_mode = True




class AddCategories(BaseModel):
    slug: str
    title_meta_tag : str
    description : str
    keywords : str
    category_order : str
    visibility : int
    show_on_main_menu : int
    show_image_on_main_menu : int
    # image : str

    class Config:
        orm_mode = True


class ProductCombinedCreate(BaseModel):
    # product fields
    slug: str
    price: int
    currency: str
    discount_rate: int
    stock: int
    attribute2_value: str
    attribute2_name: str
    attribute1_name: str
    attribute1_value: str
    attribute3_name: str
    attribute3_value: str
    attribute4_name: str
    attribute4_value: str
    product_type: str
    listing_type: str
    barcode: str
    sku: str
    shipping_charge: int
    status: int
    visibility: int

    # details fields
    title: str
    tag: str
    faqs: str
    description: str
    seo_title: str
    seo_description: str
    seo_keywords: str

