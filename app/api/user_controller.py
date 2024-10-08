from flask import Blueprint, request, jsonify
from app.repository.user_repository import UserRepository
from app.use_cases.user_use_cases import UserUseCase

user_bp = Blueprint('user', __name__)

user_repo = UserRepository()
user_use_case = UserUseCase(user_repo)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    is_admin = data.get('is_admin', False) 
    
    try:
        user_use_case.register_user(username, password, is_admin)
        return jsonify({'message': 'User registered successfully'}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    token = user_use_case.login_user(data['username'], data['password'])
    if token:
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
