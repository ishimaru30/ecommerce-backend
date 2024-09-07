from app.domain.entities.product import Product
from app.infrastructure.database import get_db

# DATABASE = 'ecommerce.db'

# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect(DATABASE)
#         g.db.execute('''CREATE TABLE IF NOT EXISTS products
#                             (id INTEGER PRIMARY KEY, name TEXT, description TEXT, price REAL, stock INTEGER)''')
#     return g.db

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
            products.append(Product(id=row['id'], name=row[1], description=row[2], price=row[3], stock=row[4]))
        return products
    
    def get_product_by_id(self, product_id):
        conn = get_db()
        cursor = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,))
        row = cursor.fetchone()
        if row:
            return Product(id=row['id'], name=row['name'], description=row['description'], price=row['price'], stock=row['stock'])
        return None