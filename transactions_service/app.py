# Entry point for the transactions microservice.  It creates a
# Flask application that registers the transactions blueprint from
# the original POS backend.  Routes provided by this blueprint
# handle transaction listing, creation, update and deletion.  The
# business logic for stock adjustment and receipt generation is
# imported unchanged.

import os
import sys
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

sys.path.append(os.path.join(os.path.dirname(__file__), 'flask_app'))

from config import Config
from transactions.routes import transactions_bp

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
jwt = JWTManager(app)

app.register_blueprint(transactions_bp, url_prefix='/api')

@app.route('/')
def health():
    return {'status': 'transactions service running'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
