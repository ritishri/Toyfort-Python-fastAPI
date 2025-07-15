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


