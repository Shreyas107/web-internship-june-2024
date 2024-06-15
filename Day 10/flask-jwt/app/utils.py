import hashlib
from flask import jsonify

def create_response(message, status=200):
    return jsonify({"message": message}), status

# Function to hash a password using SHA-256 algorithm and return the hexadecimal digest
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
