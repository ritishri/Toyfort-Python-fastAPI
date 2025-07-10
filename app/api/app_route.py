from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth_schema import UserCreate,TokenResponse,Login
from app.schemas.products_schema import ProductResponse,ProductResponseBySlug,sliderResponse
from app.services import auth_service,product_service
from app.db.database import SessionLocal


router = APIRouter(prefix="/users")

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


@router.get("/products/{slug}",response_model=list[ProductResponseBySlug])
def product_response_by_slug(slug:str,db:Session=Depends(get_db)):
    product = product_service.fetch_products_by_slug(db,slug)
    if not product:
        raise HTTPException(status_code=404,detail="Product not found")
    
    return product


@router.get("/",response_model=list[sliderResponse])
def get_home_slider(db:Session=Depends(get_db)):
     return product_service.fetch_slider(db)

