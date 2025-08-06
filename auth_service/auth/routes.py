from flask import Blueprint, request, jsonify
from ..common.database.db import users_db, logs_db
from ..common.config import Config
from .models import User
from .utils import generate_token
import uuid
from datetime import datetime

# Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'admin')
    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    existing = users_db.find_one({'username': username})
    if existing:
        return jsonify({'message': 'Username already exists'}), 400
    user_doc = {
        'id': str(uuid.uuid4()),
        'username': username,
        'password': User.generate_hash(password),
        'role': role,
        'permissions': User.get_permissions_for_role(role),
        'created_at': datetime.utcnow(),
    }
    users_db.insert_one(user_doc)
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    user = users_db.find_one({'username': username})
    if user and User.verify_hash(password, user['password']):
        token = generate_token(user)
        return jsonify({'token': token, 'user': {'id': user['id'], 'username': user['username'], 'role': user['role'], 'permissions': user.get('permissions', {})}}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/change-password', methods=['POST'])
def change_password():
    data = request.get_json() or {}
    user_id = data.get('id')
    old_password = data.get('old_password')
    new_password = data.get('new_password')
    if not user_id or not old_password or not new_password:
        return jsonify({'message': 'Missing parameters'}), 400
    user = users_db.find_one({'id': user_id})
    if not user or not User.verify_hash(old_password, user['password']):
        return jsonify({'message': 'Invalid user or password'}), 400
    users_db.update_one({'id': user_id}, {'$set': {'password': User.generate_hash(new_password)}})
    return jsonify({'message': 'Password updated successfully'}), 200

@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json() or {}
    username = data.get('username')
    user = users_db.find_one({'username': username})
    if not user:
        return jsonify({'message': 'User not found'}), 404
    temp_password = str(uuid.uuid4())[:8]
    users_db.update_one({'id': user['id']}, {'$set': {'password': User.generate_hash(temp_password)}})
    return jsonify({'message': 'Temporary password generated', 'temporary_password': temp_password}), 200

@auth_bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users_db.find_one({'id': user_id}, {'_id': 0, 'password': 0})
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user), 200

@auth_bp.route('/getUserId/<username>', methods=['GET'])
def get_user_id(username):
    user = users_db.find_one({'username': username})
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'id': user['id']}), 200
