from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Import local Config and blueprint
from .common.config import Config
from .profile.routes import profile_bp

def create_app():
    """Factory to create and configure the Flask application for the profile service."""
    app = Flask(__name__)
    CORS(app)
    # Configure JWT using the local secret key
    app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY
    jwt = JWTManager(app)

    # Register the profile blueprint under /api
    app.register_blueprint(profile_bp, url_prefix="/api")

    @app.route("/health", methods=["GET"])
    def health():
        """Health endpoint to verify service is running"""
        return {"status": "profile service healthy"}

    return app


if __name__ == "__main__":
    # Run the service with a default port; override via environment if needed
    app = create_app()
    app.run(host="0.0.0.0", port=5003, debug=True)
