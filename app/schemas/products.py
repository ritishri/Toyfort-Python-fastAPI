from pydantic import BaseModel

class ProductResponse(BaseModel):
    id : int
    slug : str
    price : int
    currency : str
    discount_rate : int
    stock : int 
    slug : str   
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

# class sliderResponse(BaseModel):
#     id : int
#     link : str
#     image : str     

#     class Config:
#         orm_code = True