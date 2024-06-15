from flask import Blueprint, request, jsonify
from .models import User
from .db import db
from .utils import create_response, hash_password
from flask_jwt_extended import create_access_token
import datetime

# a Blueprint is a way to organize and group related routes, handlers, and templates into modular components.
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    # Extract JSON data from the request body
    data = request.get_json()

    # Hash the password using a utility function
    hashed_password = hash_password(data['password'])

    # Create a new User object with the provided data
    new_user = User(name=data['name'], email=data['email'], password=hashed_password)

    db.session.add(new_user)
    db.session.commit()
    return create_response("User registered successfully", 201)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Query the database for a user with the provided email
    user = User.query.filter_by(email=data['email']).first()
    if user and user.password == hash_password(data['password']):

        # Generate an access token with the user's id as the identity
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=user.id, expires_delta=expires)
        return create_response({"token": access_token, "user_name": user.name})
    return create_response("Invalid credentials", 401)
