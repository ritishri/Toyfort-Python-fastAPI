from pydantic import BaseModel

class ProductResponse(BaseModel):
    id : int
    slug : str
    price : int
    currency : str
    discount_rate : int
    stock : int
    
    class Config:
        orm_mode = True
