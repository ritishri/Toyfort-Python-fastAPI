from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services import order_service,product_service
from app.core.auth_dependency import get_current_user
from app.schemas.products_schema import ProductCreate,ProductUpdate
router = APIRouter(prefix="/admin")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get("/")
def test_admin():
    return {"message": "Admin route working"}

@router.get("/orders/{seller_id}")
def admin_orders(seller_id:int,db:Session=Depends(get_db)):
       return order_service.order_summary(db,seller_id)


@router.post("/add-products")
def create_product(product: ProductCreate,db: Session = Depends(get_db),current_user: dict = Depends(get_current_user) 
):
    user_id = current_user["id"]  
    return product_service.create_product_service(db, product, user_id)   

@router.put("/products/{product_id}")
def update_product_endpoint( product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)  
):
    user_id = current_user["id"]
    
    updated_product = update_product_service(db, product_id, user_id, product_update.dict(exclude_unset=True))
    
    if not updated_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found or you don't have permission"
        )
    
    return {
        "success": True,
        "data": updated_product
    }        
