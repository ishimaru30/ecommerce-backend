from app.repository.user_repository import UserRepository
from app.domain.entities.user import User
from app.infrastructure.hashing import hash_password, verify_password
from app.infrastructure.jwt_handler import encode_auth_token

class UserUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, username, password, is_admin=False):
        if self.user_repo.get_user(username):
            raise ValueError("User already exists")
        password_hash = hash_password(password)
        user = User(id=None, username=username, password_hash=password_hash, is_admin=is_admin)
        self.user_repo.add_user(user)

    def login_user(self, username, password):
        user = self.user_repo.get_user(username)
        if user and verify_password(password, user.password_hash):
            token = encode_auth_token(user.id) 
            return token
        return None
