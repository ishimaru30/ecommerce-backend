from functools import wraps
from flask import request, jsonify
from app.infrastructure.jwt_handler import decode_auth_token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Bearer token

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            current_user = decode_auth_token(token)
            if isinstance(current_user, str):  # If it's a string, there's an error
                return jsonify({'message': current_user}), 403
        except:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(current_user, *args, **kwargs)

    return decorated
