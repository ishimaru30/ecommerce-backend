import unittest
from app.repository.user_repository import UserRepository
from app.use_cases.user_use_cases import UserUseCase
from app.infrastructure.hashing import hash_password
from flask import Flask
class TestUserUseCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Reset the user repository with an in-memory database for each test
        self.user_repo = UserRepository(':memory:')
        self.user_use_case = UserUseCase(self.user_repo)

    def tearDown(self):
        self.app_context.pop()

    def test_register_user(self):
        self.user_use_case.register_user('testuser2', 'password')
        user = self.user_repo.get_user('testuser2')
        self.assertIsNotNone(user)

    def test_register_user_already_exists(self):
        self.user_use_case.register_user('testuser', 'password')
        with self.assertRaises(ValueError):
            self.user_use_case.register_user('testuser', 'password')

    def test_login_user(self):
        self.user_use_case.register_user('testuser', 'password')
        token = self.user_use_case.login_user('testuser', 'password')
        self.assertIsNotNone(token)

    def test_token_generation(self):
        self.user_use_case.register_user('testuser', 'password')
        token = self.user_use_case.login_user('testuser', 'password')
        self.assertIsNotNone(token)


def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app
