from flask import Blueprint, request, jsonify
from app.repository.product_repository import ProductRepository
from app.use_cases.product_use_cases import ProductUseCase

product_bp = Blueprint('product', __name__)

product_repo = ProductRepository()
product_use_case = ProductUseCase(product_repo)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = product_use_case.get_products()
    return jsonify([product.__dict__ for product in products]), 200

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    product_use_case.add_product(data['name'], data['description'], data['price'], data['stock'])
    return jsonify({'message': 'Product added successfully'}), 201
