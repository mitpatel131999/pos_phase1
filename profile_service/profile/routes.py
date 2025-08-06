"""
Routes for the profile microservice.  These endpoints allow
clients to retrieve and update profile information for the
currently authenticated user.  Additional routes for settings,
pending transactions and sessions can be implemented similarly.

This blueprint depends only on local modules and MongoDB
collections defined in the common.database package.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# Import database collections from the common package
from ..common.database.db import (
    profiles_col,
    settings_col,
    pending_transactions_col,
    sessions_col,
    users_col,
    logs_col,
)

profile_bp = Blueprint("profile_bp", __name__)


@profile_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    """Return the current user's profile or a default structure."""
    user_id = get_jwt_identity()
    profile = profiles_col.find_one({"userId": user_id})
    if profile:
        profile["_id"] = str(profile["_id"])
        return jsonify(profile), 200
    # Default profile structure if none exists
    default_profile = {
        "userId": user_id,
        "firstName": "",
        "lastName": "",
        "email": "",
        "phone": "",
        "address": "",
    }
    return jsonify(default_profile), 200


@profile_bp.route("/profile", methods=["POST"])
@jwt_required()
def update_profile():
    """Create or update the current user's profile."""
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    data["userId"] = user_id
    profiles_col.update_one({"userId": user_id}, {"$set": data}, upsert=True)
    return jsonify({"message": "Profile updated successfully"}), 200


@profile_bp.route("/settings", methods=["GET"])
@jwt_required()
def get_settings():
    """Return user-specific settings or defaults."""
    user_id = get_jwt_identity()
    settings = settings_col.find_one({"userId": user_id})
    if settings:
        settings["_id"] = str(settings["_id"])
        return jsonify(settings), 200
    default_settings = {
        "userId": user_id,
        "camera": True,
        "scanner": True,
    }
    return jsonify(default_settings), 200


@profile_bp.route("/settings", methods=["POST"])
@jwt_required()
def update_settings():
    """Update user-specific POS settings."""
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    data["userId"] = user_id
    settings_col.update_one({"userId": user_id}, {"$set": data}, upsert=True)
    return jsonify({"message": "Settings updated successfully"}), 200
