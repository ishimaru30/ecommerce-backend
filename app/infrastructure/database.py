import sqlite3
from flask import g

DATABASE = 'ecommerce.db'

def get_db():
    """
    Opens a new database connection if one does not already exist for the current request.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  # This allows for easier row access by column name
    return g.db

def close_db(e=None):
    """
    Closes the database connection for the current request.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()
