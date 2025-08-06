# Entry point for the catalog (products) microservice.  It sets up
# a Flask application and registers the products blueprint from
# the original POS backend.  This blueprint includes endpoints for
# product CRUD operations, suppliers, purchase orders and image
# uploads.  Business logic is imported unchanged from the
# monolithic codebase.

import os
import sys
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

sys.path.append(os.path.join(os.path.dirname(__file__), 'flask_app'))

from config import Config
from products.routes import products_bp

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
jwt = JWTManager(app)

# Register the products blueprint with the `/api` prefix to match
# the original API surface.  Within the blueprint, routes use
# their own additional prefixes (e.g. /products, /online-products).
app.register_blueprint(products_bp, url_prefix='/api')

@app.route('/')
def health():
    return {'status': 'catalog service running'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
