"""
Entry point for the authentication microservice.
This Flask application uses local modules instead of cloning
code from the original repository. Only authentication routes
are registered here.
"""

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Import configuration and authentication blueprint from local modules
from .common.config import Config
from .auth.routes import auth_bp


def create_app() -> Flask:
    """Factory pattern to create and configure the Flask app."""
    app = Flask(__name__)
    CORS(app)

    # Load configuration from the local Config class
    app.config.from_object(Config)
    # Ensure JWT secret is set for token operations
    app.config.setdefault("JWT_SECRET_KEY", Config.SECRET_KEY)

    # Initialise JWT handling
    jwt = JWTManager(app)

    # Register the authentication blueprint at its url_prefix
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    # Health check endpoint
    @app.route("/health", methods=["GET"])
    def health() -> dict:
        return {"status": "auth service healthy"}

    return app


# Allow running the app with `python app.py` for debugging
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
