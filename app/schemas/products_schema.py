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
    id : int
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
    product_type: str
    listing_type: str
    barcode: str
    sku: str
    shipping_charge: int
    status: int
    visibility: int
    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    slug: Optional[str]
    price: Optional[int]
    currency: Optional[str]
    discount_rate: Optional[int]
    stock: Optional[int]
    product_type: Optional[str]
    listing_type: Optional[str]
    barcode: Optional[str]
    sku: Optional[str]
    shipping_charge: Optional[int]
    status: Optional[int]
    visibility: Optional[int]

    class Config:
        orm_mode = True