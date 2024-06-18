from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from utils import create_success_response, create_error_response
from config import SECRET_KEY, PORT_NO
import jwt
from db import init_db

app = Flask(__name__)
CORS(app)

# Setting up logging
logging.basicConfig(level=logging.INFO)

# Initialize the database
mysql = init_db(app)

# Return version
@app.route("/version", methods=["GET"])
def version():
    return jsonify(create_success_response("1.0"))

# Middleware for protected routes
@app.before_request
def require_authorization():
    skip_urls = ["/user/login", "/user/register", "version"]
    if request.path in skip_urls:
        return None

    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify(create_error_response("missing authorization header")), 401

    token = auth_header.split(" ")[1]
    if not token:
        return jsonify(create_error_response("missing token")), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        request.data = payload
    except jwt.ExpiredSignatureError:
        return jsonify(create_error_response("expired token")), 401
    except jwt.InvalidTokenError:
        return jsonify(create_error_response("invalid token")), 401

# Add Routes
from routes.user import user_bp
app.register_blueprint(user_bp, url_prefix="/user")

if __name__ == "__main__":
    app.run(port=PORT_NO)
