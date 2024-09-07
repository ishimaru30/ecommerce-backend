import sqlite3
from flask import g

DATABASE = 'ecommerce.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.execute('''CREATE TABLE IF NOT EXISTS orders
                            (id INTEGER PRIMARY KEY, user_id INTEGER, product_data TEXT)''')
    return g.db

class OrderRepository:
    def __init__(self, db_path='ecommerce.db'):  # Default to the file database
        self.db_path = db_path
        
    def save_order(self, user_id, product_data):
        conn = get_db()
        conn.execute('INSERT INTO orders (user_id, product_data) VALUES (?, ?)', (user_id, product_data))
        conn.commit()

    def get_orders_by_user(self, user_id):
        conn = get_db()
        cursor = conn.execute('SELECT * FROM orders WHERE user_id = ?', (user_id,))
        orders = []
        for row in cursor:
            orders.append({'id': row[0], 'user_id': row[1], 'product_data': row[2]})
        return orders
    
    def get_cart_items(self, user_id):
        return self.cart.get(user_id, [])

    def add_to_cart(self, user_id, cart_items):
        if user_id not in self.cart:
            self.cart[user_id] = []
        self.cart[user_id].extend(cart_items)