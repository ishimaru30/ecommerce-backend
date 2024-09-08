from flask import Blueprint, request, jsonify
from app.repository.product_repository import ProductRepository
from app.use_cases.product_use_cases import ProductUseCase
from app.infrastructure.auth_middleware import token_required, admin_required

product_bp = Blueprint('product', __name__)

product_repo = ProductRepository()
product_use_case = ProductUseCase(product_repo)

# Admin: Add a new product
@product_bp.route('/products', methods=['POST'])
@admin_required
def add_product():
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data or 'stock' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    name = data['name']
    description = data.get('description', '')
    price = data['price']
    stock = data['stock']

    product_use_case.add_product(name, description, price, stock)
    return jsonify({'message': 'Product added successfully'}), 201

# Admin: Edit a product
@product_bp.route('/products/<int:product_id>', methods=['PUT'])
@admin_required
def edit_product(product_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing required fields'}), 400

    updated_fields = {}
    if 'name' in data:
        updated_fields['name'] = data['name']
    if 'description' in data:
        updated_fields['description'] = data['description']
    if 'price' in data:
        updated_fields['price'] = data['price']
    if 'stock' in data:
        updated_fields['stock'] = data['stock']

    product_use_case.update_product(product_id, updated_fields)
    return jsonify({'message': 'Product updated successfully'}), 200

# Admin: Remove a product
@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
@admin_required
def delete_product(product_id):
    product_use_case.delete_product(product_id)
    return jsonify({'message': 'Product deleted successfully'}), 200
