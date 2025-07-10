from sqlalchemy.orm import Session
from app.model.auth_model import User


def getUserEmail(db:Session, email:str):
    return db.query(User).filter(User.email == email).first()

def createUser(db:Session, first_name:str, last_name:str,email:str,password:str):
    user = User(first_name=first_name,last_name=last_name,email=email,password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
