import jwt
import datetime

SECRET_KEY = '5c750dfc0cfd0b623427f891a59a2c10ad132374d9375efedbe567c830983d02' 

def encode_auth_token(user_id):
    """
    Generates the Auth Token using the user's ID.
    """
    try:
        payload = {
            'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=1),  # Use timezone-aware UTC datetime
            'iat': datetime.datetime.now(datetime.UTC),  # Use timezone-aware UTC datetime
            'sub': user_id
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    """
    try:
        payload = jwt.decode(auth_token, SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
