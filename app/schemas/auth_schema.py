from pydantic import BaseModel,EmailStr,constr

class UserCreate(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    phone_number: constr(min_length=10, max_length=10, pattern=r'^\d{10}$')    
    password:str
    confirm_password:str 

class Login(BaseModel):
    email:EmailStr
    password:str    

class TokenResponse(BaseModel):
    id:int 
    access_token: str
    token_type: str

    class Config:
        orm_mode = True   