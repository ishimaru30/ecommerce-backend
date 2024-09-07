import unittest
from flask import Flask
from app.repository.order_repository import OrderRepository
from app.use_cases.order_use_cases import OrderUseCase
from app.infrastructure.database import get_db, close_db

class TestOrderUseCase(unittest.TestCase):
    def setUp(self):
        # Create a Flask app and push the context for each test
        self.app = create_app()  # Create a Flask app instance
        self.app_context = self.app.app_context()  # Create app context
        self.app_context.push()  # Push the context to use Flask's 'g'

        # Set up the order repository and use case with an in-memory database
        self.order_repo = OrderRepository()
        self.order_use_case = OrderUseCase(self.order_repo)
        self._clear_database()  # Ensure a clean state

    def tearDown(self):
        # Pop the app context after each test and close the DB
        close_db()
        self.app_context.pop()

    def _clear_database(self):
        # Clear the orders table before each test
        conn = get_db()
        conn.execute('DELETE FROM orders')
        conn.commit()

    def test_place_order(self):
        user_id = 1
        cart_items = [{'product_id': 1, 'quantity': 2}]
        self.order_use_case.place_order(user_id, cart_items)
        orders = self.order_use_case.get_orders_by_user(user_id)
        self.assertEqual(len(orders), 1)
        
if __name__ == '__main__':
    unittest.main()

# Create a Flask app for testing
def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app
