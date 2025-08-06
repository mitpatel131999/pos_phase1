# Entry point for the profile/session microservice.  It creates a
# Flask application that registers the profile blueprint from the
# original POS backend.  The registered routes handle profile
# retrieval and update, settings, pending transactions and session
# management.  Business logic is imported from the monolith and
# remains unchanged.

import os
import sys

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

sys.path.append(os.path.join(os.path.dirname(__file__), 'flask_app'))

from config import Config
from profile.routes import profile_bp

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
jwt = JWTManager(app)

app.register_blueprint(profile_bp, url_prefix='/api')

@app.route('/')
def health():
    return {'status': 'profile service running'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
