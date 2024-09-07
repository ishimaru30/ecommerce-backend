from flask import json
from app.infrastructure.database import get_db

class OrderRepository:
    def __init__(self, db_path='ecommerce.db'):  
        self.db_path = db_path
        
    def save_order(self, user_id, product_data):
        conn = get_db()
        serialized_data = json.dumps(product_data) 
        conn.execute('INSERT INTO orders (user_id, product_data) VALUES (?, ?)', (user_id, serialized_data))
        conn.commit()

    def get_orders_by_user(self, user_id):
        conn = get_db()
        cursor = conn.execute('SELECT * FROM orders WHERE user_id = ?', (user_id,))
        orders = []
        for row in cursor:
            orders.append({
                'id': row['id'],
                'user_id': row['user_id'],
                'product_data': json.loads(row['product_data'])  
            })
        return orders
    
    def get_order_by_id(self, order_id):
        conn = get_db()
        cursor = conn.execute('SELECT * FROM orders WHERE id = ?', (order_id,))
        row = cursor.fetchone()
        if row:
            return {'id': row['id'], 'user_id': row['user_id'], 'product_data': row['product_data']}
        return None
    
    def get_cart_items(self, user_id):
        return self.cart.get(user_id, [])

    def add_to_cart(self, user_id, cart_items):
        if user_id not in self.cart:
            self.cart[user_id] = []
        self.cart[user_id].extend(cart_items)