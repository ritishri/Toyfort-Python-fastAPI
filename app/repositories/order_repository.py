# from sqlalchemy.orm import Session
# from sqlalchemy import text



# def completed_order(db:Session, seller_id:int):
#     query = text("SELECT COUNT(DISTINCT o.id) FROM orders o INNER JOIN order_products op ON op.order_id = o.id WHERE op.seller_id = :seller_id AND op.order_status = 'completed';")

#     count = db.execute(query,{"seller_id":seller_id}).fetchone()
#     return count[0]


# def active_sales(db:Session, seller_id:int):
#     query = text("SELECT COUNT(DISTINCT o.id) FROM orders o INNER JOIN order_products op ON op.order_id = o.id WHERE op.seller_id = :seller_id AND op.order_status != 'completed' AND op.order_status != 'cancelled';")

#     count = db.execute(query,{"seller_id":seller_id}).fetchone()
#     return count[0]


# def page_review(db:Session, seller_id:int):
#     query = text(" SELECT SUM(products.pageviews) AS total_pageviews FROM products WHERE products.status = 1 AND products.is_draft = 0 AND products.is_deleted = 0 AND products.user_id = :seller_id;")

#     pageReview = db.execute(query,{"seller_id":seller_id}).fetchone()
#     return pageReview[0]

# def sales_by_seller_limited(db:Session,seller_id:int):
#     query = text("SELECT orders.* FROM orders INNER JOIN order_products ON order_products.order_id = orders.id WHERE order_products.seller_id = :seller_id GROUP BY orders.id ORDER BY orders.created_at DESC LIMIT 15;")

#     data = db.execute(query,{"seller_id":seller_id})
#     return data 

