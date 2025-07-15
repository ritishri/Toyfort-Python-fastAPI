from sqlalchemy.orm import Session
from sqlalchemy import text


def order_summary(db:Session,seller_id:int)->dict:

    active_sales_query = text("SELECT COUNT(DISTINCT o.id) FROM orders o INNER JOIN order_products op ON op.order_id = o.id WHERE op.seller_id = :seller_id AND op.order_status != 'completed' AND op.order_status != 'cancelled';")
    active_sales =  db.execute(active_sales_query,{"seller_id":seller_id}).scalar()

    completed_order_query = text("SELECT COUNT(DISTINCT o.id) FROM orders o INNER JOIN order_products op ON op.order_id = o.id WHERE op.seller_id = :seller_id AND op.order_status = 'completed';")
    completed_order = db.execute(completed_order_query,{"seller_id":seller_id}).scalar()

    page_review_query = text("SELECT SUM(products.pageviews) AS total_pageviews FROM products WHERE products.status = 1 AND products.is_draft = 0 AND products.is_deleted = 0 AND products.user_id = :seller_id;")
    page_review = db.execute(page_review_query,{"seller_id":seller_id}).scalar()

    sales_by_seller_query = text("SELECT orders.* FROM orders INNER JOIN order_products ON order_products.order_id = orders.id WHERE order_products.seller_id = :seller_id GROUP BY orders.id ORDER BY orders.created_at DESC LIMIT 15;")
    sales_by_seller = db.execute(sales_by_seller_query,{"seller_id":seller_id})
    recent_sales = [dict(row._mapping) for row in sales_by_seller]



    return {
        "completed-order":completed_order,
        "active-sales":active_sales,
        "total-sale":completed_order + active_sales,
        "page-review":page_review,
        "sale-summary":recent_sales
    }