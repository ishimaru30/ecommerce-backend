from app.domain.entities.user import User
from app.infrastructure.database import get_db

class UserRepository:
    def __init__(self, db_path='ecommerce.db'):  # Default to the file database
        self.db_path = db_path
        
    def add_user(self, user: User):
        conn = get_db()
        conn.execute('INSERT INTO users (username, password_hash, is_admin) VALUES (?, ?, ?)',
                     (user.username, user.password_hash, user.is_admin))
        conn.commit()

    def get_user(self, username):
        conn = get_db()
        cursor = conn.execute('SELECT * FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        if row:
            return User(id=row[0], username=row[1], password_hash=row[2], is_admin=bool(row[3]))
        return None

    
    def get_user_by_id(self, user_id):
        conn = get_db()
        cursor = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        if row:
            return User(id=row['id'], username=row['username'], password_hash=row['password_hash'], is_admin=bool(row['is_admin']))
        return None