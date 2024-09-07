import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, g
from app.infrastructure.database import close_db
from app.api.user_controller import user_bp
from app.api.product_controller import product_bp
from app.api.order_controller import order_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(product_bp, url_prefix='/product')
app.register_blueprint(order_bp, url_prefix='/order')

@app.teardown_appcontext
def teardown_db(exception):
    close_db(exception)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
