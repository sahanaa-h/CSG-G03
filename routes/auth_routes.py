from flask import Blueprint, request, jsonify
from services.auth_service import register_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    return register_user(data['username'], data['email'], data['password'])

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    return login_user(data['username'], data['password'])
