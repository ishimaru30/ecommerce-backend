import sqlite3
from flask import g
from app.domain.entities.user import User

DATABASE = 'ecommerce.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.execute('''CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY, username TEXT, password_hash TEXT, is_admin INTEGER)''')
    return g.db

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
            return User(username=row[1], password_hash=row[2], is_admin=bool(row[3]))
        return None
