from flask import Blueprint, request, jsonify
from app.repository.order_repository import OrderRepository
from app.use_cases.order_use_cases import OrderUseCase
from app.infrastructure.auth_middleware import token_required

order_bp = Blueprint('order', __name__)

order_repo = OrderRepository()
order_use_case = OrderUseCase(order_repo)

@order_bp.route('/order', methods=['POST'])
@token_required
def place_order(current_user):
    data = request.get_json()  # Get the request body as JSON
    if 'cart_items' not in data:
        return jsonify({'error': 'Missing cart_items in request body'}), 400

    cart_items = data['cart_items']
    user_id = current_user
    order_use_case.place_order(user_id, cart_items)
    return jsonify({'message': 'Order placed successfully'}), 201

@order_bp.route('/cart', methods=['GET'])
@token_required
def get_cart(current_user):
    user_id = current_user    
    orders = order_use_case.get_orders_by_user(user_id)
    
    if not orders:
        return jsonify({'message': 'Cart is empty'}), 200

    return jsonify({'orders': orders}), 200

# View Orders Endpoint
@order_bp.route('/orders', methods=['GET'])
@token_required
def view_orders(current_user):
    user_id = current_user  # Extracted from the token
    orders = order_use_case.get_orders_by_user(user_id)
    return jsonify(orders), 200
