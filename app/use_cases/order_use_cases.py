from app.repository.order_repository import OrderRepository
from app.domain.entities.order import Order

class OrderUseCase:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    def place_order(self, user_id, cart_items):
        order = Order(user_id, cart_items)
        self.order_repo.save_order(user_id=user_id, product_data=str(cart_items))
        
    def get_orders_by_user(self, user_id):
        return self.order_repo.get_orders_by_user(user_id)
    
    def get_cart_items(self, user_id):
        return self.order_repo.get_cart_items(user_id)