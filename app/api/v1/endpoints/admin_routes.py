from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services import order_service,product_service
from app.core.auth_dependency import get_current_user
from app.schemas.products_schema import ProductCreate,ProductUpdate,ProductDetailsCreate,AddCategories
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
def create_product(product: ProductCreate,product_details:ProductDetailsCreate,db: Session = Depends(get_db),current_user: dict = Depends(get_current_user) 
):
    user_id = current_user["id"]  
    return product_service.create_product_service(db, product, product_details,user_id)   

@router.put("/products/{product_id}")
def update_product_endpoint( product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)  
):
    user_id = current_user["id"]
    
    updated_product = product_service.update_product_service(db, product_id, user_id, product_update.dict(exclude_unset=True))
    
    if not updated_product:
        raise HTTPException(
            sstatus_code=404,
            detail="Product not found or you don't have permission"
        )
    
    return {
        "success": True,
        "data": updated_product
    }        



@router.post('/add-categories')
def add_categories(product_cat:AddCategories, db:Session = Depends(get_db)):
     add_cat = product_service.add_category_service(product_cat,db)
     return {
        "success": True,
        "data": add_cat
    } 
