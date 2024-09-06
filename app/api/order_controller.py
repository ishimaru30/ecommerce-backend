from flask import Blueprint, request, jsonify
from app.repository.order_repository import OrderRepository
from app.use_cases.order_use_cases import OrderUseCase

order_bp = Blueprint('order', __name__)

order_repo = OrderRepository()
order_use_case = OrderUseCase(order_repo)

@order_bp.route('/order', methods=['POST'])
def place_order():
    data = request.json
    order_use_case.place_order(data['user_id'], data['cart_items'])
    return jsonify({'message': 'Order placed successfully'}), 201
