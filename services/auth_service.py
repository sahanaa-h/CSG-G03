from werkzeug.security import generate_password_hash, check_password_hash
from models.db import db
from models.auth import User
from flask_jwt_extended import create_access_token

def register_user(username, email, password):
    """Register a new user"""
    # Check if user already exists
    user = User.query.filter_by(username=username).first()
    if user:
        return {'message': 'User already exists'}, 400

    # Hash the password before saving it
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    # Include email when creating the user
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return {'message': 'User created successfully'}, 201


def login_user(username, password):
    """Login a user and return a JWT token"""
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return {'access_token': access_token}, 200
    return {'message': 'Invalid credentials'}, 401
