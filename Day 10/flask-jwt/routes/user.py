from flask import Blueprint, request, jsonify
from utils import create_success_response, create_error_response
import hashlib
import jwt
from config import SECRET_KEY
from db import mysql

user_bp = Blueprint("user", __name__)

# REGISTER API
@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    encrypted_password = hashlib.sha256(password.encode()).hexdigest()
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(query, (name, email, encrypted_password))
        mysql.connection.commit()
        cursor.close()
        return jsonify(create_success_response("User registered successfully"))
    except Exception as e:
        return jsonify(create_error_response(str(e)))

# LOGIN API
@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    encrypted_password = hashlib.sha256(password.encode()).hexdigest()
    query = "SELECT id, name, email FROM users WHERE email = %s AND password = %s"

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(query, (email, encrypted_password))
        user = cursor.fetchone()
        cursor.close()

        if not user:
            return jsonify(create_error_response("User not found!"))

        payload = {
            "user_id": user[0],
            "user_name": user[1],
            "user_email": user[2],
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return jsonify(create_success_response({"token": token, "user_name": user[1]}))
    except Exception as e:
        return jsonify(create_error_response(str(e)))

# Protected route example
@user_bp.route("/students", methods=["GET"])
def students():
    query = "SELECT * FROM students"
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        students = cursor.fetchall()
        cursor.close()
        return jsonify(create_success_response(students))
    except Exception as e:
        return jsonify(create_error_response("Database error"))
