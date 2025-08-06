# Entry point for the authentication microservice.  It constructs
# a minimal Flask application, configures CORS, loads the
# application configuration from the original project and
# registers only the authentication blueprint.  Business logic
# remains untouched: all routes and handlers are imported from the
# original codebase.

import os
import sys

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Add the cloned flask_app directory to sys.path so we can import
# modules directly from the original project.  The PYTHONPATH
# environment variable is set in the Dockerfile, but adding here
# ensures local execution also works.
sys.path.append(os.path.join(os.path.dirname(__file__), 'flask_app'))

from config import Config
from auth.routes import auth_bp

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

# Initialise JWT handling.  The configuration loaded above
# includes the JWT secret key from the original project.
jwt = JWTManager(app)

# Register only the authentication blueprint at its original
# prefix.  All routes under `/api/auth` will be served by this
# service.
app.register_blueprint(auth_bp, url_prefix='/api/auth')

@app.route('/')
def health():
    return {'status': 'auth service running'}

if __name__ == '__main__':
    # Bind to 0.0.0.0 so that the container is reachable from
    # outside.  In production you might use a production WSGI
    # server instead of Flask’s development server.
    app.run(host='0.0.0.0', port=5000)
