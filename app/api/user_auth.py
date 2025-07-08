from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate,TokenResponse,Login
from app.schemas.products import ProductResponse
from app.services import auth_service
from app.services import product_service
from app.db.database import SessionLocal


router = APIRouter(prefix="/users",tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/test")
def test():
    return {"message": "User route working"}


@router.post("/register",response_model=TokenResponse)
def register(user:UserCreate, db:Session=Depends(get_db)):
    return auth_service.register_user(db,user)  


@router.post("/login")
def login(data:Login,db: Session = Depends(get_db)):
    return auth_service.login(db,data.email,data.password)


@router.get("/product",response_model=list[ProductResponse])
def login(db: Session = Depends(get_db)):
    return product_service.fetch_products(db)
