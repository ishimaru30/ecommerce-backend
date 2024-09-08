from app.domain.entities.product import Product
from app.infrastructure.database import get_db

class ProductRepository:
    def __init__(self, db_path='ecommerce.db'): 
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
    
    def update_product(self, product_id, updated_fields):
        conn = get_db()
        set_clause = ', '.join(f"{key} = ?" for key in updated_fields)
        values = list(updated_fields.values()) + [product_id]
        query = f"UPDATE products SET {set_clause} WHERE id = ?"
        conn.execute(query, values)
        conn.commit()

    def delete_product(self, product_id):
        conn = get_db()
        conn.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()