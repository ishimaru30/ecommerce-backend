import sqlite3
from flask import g

DATABASE = 'ecommerce.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row 

        # Create tables if they don't exist
        g.db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password_hash TEXT,
                is_admin INTEGER
            )
        ''')
        
        g.db.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                price REAL,
                stock INTEGER
            )
        ''')
        
        g.db.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                product_data TEXT
            )
        ''')
    return g.db


def close_db(e=None):
    """
    Closes the database connection for the current request.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()
