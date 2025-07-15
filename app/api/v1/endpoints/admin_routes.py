from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services import order_service 
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
