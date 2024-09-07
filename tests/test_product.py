import unittest
from flask import Flask
from app.repository.product_repository import ProductRepository
from app.use_cases.product_use_cases import ProductUseCase
from app.infrastructure.database import get_db, close_db

class TestProductUseCase(unittest.TestCase):

    def setUp(self):
        # Create the Flask app and push the application context
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Setup repositories and use cases
        self.product_repo = ProductRepository()
        self.product_use_case = ProductUseCase(self.product_repo)
        self._clear_database()

    def tearDown(self):
        # Close the connection after each test and pop the app context
        close_db()
        self.app_context.pop()

    def _clear_database(self):
        conn = get_db()
        conn.execute('DELETE FROM products')
        conn.commit()

    def test_add_product(self):
        self.product_use_case.add_product('Test Product', 'A test product', 10.99, 5)
        products = self.product_use_case.get_products()
        self.assertEqual(len(products), 1)

    def test_get_products(self):
        self.product_use_case.add_product('Product 1', 'Description 1', 10.99, 5)
        self.product_use_case.add_product('Product 2', 'Description 2', 15.99, 10)
        products = self.product_use_case.get_products()
        self.assertEqual(len(products), 2)

if __name__ == '__main__':
    unittest.main()
