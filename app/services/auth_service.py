from sqlalchemy.orm import Session
from app.schemas.auth_schema import UserCreate
from app.repositories import auth_repository
from fastapi import HTTPException, status
import bcrypt
from app.core import jwt_token

def register_user(db:Session, user:UserCreate):

    if user.confirm_password != user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Password not match")
    
    existingUser = auth_repository.getUserEmail(db,user.email)
    if existingUser:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered") 
    
    if len(user.phone_number) > 10:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Phone number must be at most 10 characters"
    )
    hashed_password = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())

    registered_user = auth_repository.createUser(db,user.first_name,user.last_name,user.email,hashed_password)

    token = jwt_token.create_token({
        "id":registered_user.id,
        "email":registered_user.email
    })

    return {
        "success":True,
        "id":registered_user.id,
        "access_token":token,
        "token_type":"bearer"
    }


def login(db:Session, email:str,password:str):
    if not email or not password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Provide an email and password")
    
    user = auth_repository.getUserEmail(db,email)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User not found with this email")
    
    isMatch = bcrypt.checkpw(password.encode(),user.password.encode())

    if not isMatch:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")
    
    token = jwt_token.create_token({
        "id":user.id,
        "email":user.email
    })

    return {
        "success":True,
        "data":{
            "id": user.id,
            "name": user.first_name,
            "email": user.email,
            "token": token
        }
    }