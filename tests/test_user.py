import unittest
from app.repository.user_repository import UserRepository
from app.use_cases.user_use_cases import UserUseCase
from app.infrastructure.hashing import hash_password

class TestUserUseCase(unittest.TestCase):
    def setUp(self):
        # Using in-memory SQLite database for testing
        self.user_repo = UserRepository(':memory:')
        self.user_use_case = UserUseCase(self.user_repo)

    def test_register_user(self):
        # Register a new user
        self.user_use_case.register_user('testuser', 'password')
        
        # Fetch user from the repository
        user = self.user_repo.get_user('testuser')
        
        # Assert user is successfully registered
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')

    def test_register_user_already_exists(self):
        # Register the same user twice
        self.user_use_case.register_user('testuser', 'password')
        with self.assertRaises(ValueError):
            self.user_use_case.register_user('testuser', 'password')

    def test_login_user(self):
        # Register and login a user
        self.user_use_case.register_user('testuser', 'password')
        result = self.user_use_case.login_user('testuser', 'password')
        
        # Assert login is successful
        self.assertTrue(result)

    def test_login_invalid_user(self):
        # Test login with invalid credentials
        result = self.user_use_case.login_user('invaliduser', 'password')
        
        # Assert login fails
        self.assertFalse(result)

    def test_login_invalid_password(self):
        # Register a user
        self.user_use_case.register_user('testuser', 'password')
        
        # Try logging in with incorrect password
        result = self.user_use_case.login_user('testuser', 'wrongpassword')
        
        # Assert login fails
        self.assertFalse(result)
