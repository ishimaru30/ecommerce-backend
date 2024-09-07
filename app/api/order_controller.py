from flask import Blueprint, request, jsonify
from app.repository.order_repository import OrderRepository
from app.use_cases.order_use_cases import OrderUseCase
from app.infrastructure.auth_middleware import token_required

order_bp = Blueprint('order', __name__)

order_repo = OrderRepository()
order_use_case = OrderUseCase(order_repo)

# Place Order Endpoint
@order_bp.route('/order', methods=['POST'])
@token_required
def place_order(current_user):
    data = request.json
    user_id = current_user  # Extracted from the token
    cart_items = data['cart_items']
    order_id = order_use_case.place_order(user_id, cart_items)  # Return the order ID
    return jsonify({'message': 'Order placed successfully', 'order_id': order_id}), 201


# View Cart Endpoint
@order_bp.route('/cart', methods=['GET'])
@token_required
def view_cart(current_user):
    user_id = current_user  # Extracted from the token
    cart_items = order_use_case.get_cart_items(user_id)
    return jsonify(cart_items), 200

# View Orders Endpoint
@order_bp.route('/orders', methods=['GET'])
@token_required
def view_orders(current_user):
    user_id = current_user  # Extracted from the token
    orders = order_use_case.get_orders_by_user(user_id)
    return jsonify(orders), 200
