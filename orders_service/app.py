# Entry point for the orders microservice.  It registers the
# orders blueprint from the original POS backend with the Flask
# application.  Endpoints exposed by this service handle order
# creation, listing and status updates.  Business logic remains
# intact and is imported from the monolith.

import os
import sys
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

sys.path.append(os.path.join(os.path.dirname(__file__), 'flask_app'))

from config import Config
from orders.routes import orders_bp

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
jwt = JWTManager(app)

# Register the orders blueprint with the `/api` prefix to match
# the original API surface.
app.register_blueprint(orders_bp, url_prefix='/api')

@app.route('/')
def health():
    return {'status': 'orders service running'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
