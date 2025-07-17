from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services import order_service,product_service
from app.core.auth_dependency import get_current_user
from app.schemas.products_schema import ProductUpdate,AddCategories,ProductCombinedCreate
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
def create_product_route(
    combined_data: ProductCombinedCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    user_id = current_user["id"]
    new_prod = product_service.create_product_service(db, combined_data, user_id)
    return {
        "success": True,
    } 



@router.put("/update-products/{product_id}")
def update_product_endpoint( product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)  
):
    user_id = current_user["id"]
    
    updated_product = product_service.update_product_service(db, product_id, user_id, product_update.dict(exclude_unset=True))
    
    if not updated_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
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
