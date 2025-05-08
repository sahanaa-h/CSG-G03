from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    result = register_user(username, password)
    return jsonify(result)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    result = login_user(username, password)
    return jsonify(result)
