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
    data = request.json
    user_id = current_user  # Extracted from the token
    cart_items = data['cart_items']
    order_use_case.place_order(user_id, cart_items)
    return jsonify({'message': 'Order placed successfully'}), 201
