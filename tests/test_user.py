import unittest
from app.repository.user_repository import UserRepository
from app.use_cases.user_use_cases import UserUseCase
from app.infrastructure.database import get_db, close_db
from flask import Flask

class TestUserUseCase(unittest.TestCase):

    def setUp(self):
        # Create the Flask app and push the application context
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Setup repositories and use cases
        self.user_repo = UserRepository()
        self.user_use_case = UserUseCase(self.user_repo)
        self._clear_database()

    def tearDown(self):
        # Clear the database and pop the app context
        close_db()
        self.app_context.pop()

    def _clear_database(self):
        conn = get_db()
        conn.execute('DELETE FROM users')
        conn.commit()

    def test_register_user_success(self):
        self.user_use_case.register_user('testuser', 'password')
        user = self.user_repo.get_user('testuser')
        self.assertIsNotNone(user)

    def test_login_user_success(self):
        self.user_use_case.register_user('testuser', 'password')
        token = self.user_use_case.login_user('testuser', 'password')
        self.assertIsNotNone(token)

    def test_login_invalid_credentials(self):
        self.user_use_case.register_user('testuser', 'password')
        token = self.user_use_case.login_user('testuser', 'wrongpassword')
        self.assertIsNone(token)

    def test_register_user_already_exists(self):
        self.user_use_case.register_user('testuser', 'password')
        with self.assertRaises(ValueError):
            self.user_use_case.register_user('testuser', 'password')

if __name__ == '__main__':
    unittest.main()
