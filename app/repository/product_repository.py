import sqlite3
from flask import g
from app.domain.entities.product import Product

DATABASE = 'ecommerce.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.execute('''CREATE TABLE IF NOT EXISTS products
                            (id INTEGER PRIMARY KEY, name TEXT, description TEXT, price REAL, stock INTEGER)''')
    return g.db

class ProductRepository:
    def __init__(self, db_path='ecommerce.db'):  # Default to the file database
        self.db_path = db_path
        
    def add_product(self, product: Product):
        conn = get_db()
        conn.execute('INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?)',
                     (product.name, product.description, product.price, product.stock))
        conn.commit()

    def get_all_products(self):
        conn = get_db()
        cursor = conn.execute('SELECT * FROM products')
        products = []
        for row in cursor:
            products.append(Product(name=row[1], description=row[2], price=row[3], stock=row[4]))
        return products
