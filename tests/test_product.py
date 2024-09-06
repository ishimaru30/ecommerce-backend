import unittest
from app.repository.product_repository import ProductRepository
from app.use_cases.product_use_cases import ProductUseCase
from app.domain.entities.product import Product

class TestProductUseCase(unittest.TestCase):
    def setUp(self):
        self.product_repo = ProductRepository(':memory:')
        self.product_use_case = ProductUseCase(self.product_repo)

    def test_add_product(self):
        self.product_use_case.add_product('Test Product', 'A test product', 10.99, 5)
        products = self.product_use_case.get_products()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, 'Test Product')

    def test_get_products(self):
        self.product_use_case.add_product('Product 1', 'Description 1', 10.99, 5)
        self.product_use_case.add_product('Product 2', 'Description 2', 15.99, 10)
        products = self.product_use_case.get_products()
        self.assertEqual(len(products), 2)
        self.assertEqual(products[1].name, 'Product 2')
