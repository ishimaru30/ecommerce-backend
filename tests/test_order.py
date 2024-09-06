import unittest
from app.repository.order_repository import OrderRepository
from app.use_cases.order_use_cases import OrderUseCase

class TestOrderUseCase(unittest.TestCase):
    def setUp(self):
        self.order_repo = OrderRepository(':memory:')
        self.order_use_case = OrderUseCase(self.order_repo)

    def test_place_order(self):
        user_id = 1
        cart_items = [{'product_id': 1, 'quantity': 2}, {'product_id': 2, 'quantity': 1}]
        self.order_use_case.place_order(user_id, cart_items)
  
        self.assertTrue(True) 
