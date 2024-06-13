from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Function to create and return a connection to the MySQL database
def create_connection():
    connection = None
    try:
        # Establish connection to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='shreyas',
            database='intern'
        )
        if connection.is_connected():
            print("MySQL Database connected")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)  # Use dictionary cursor to get results as dictionaries
    cursor.execute("SELECT * FROM users")  # Execute SQL query to fetch all users
    rows = cursor.fetchall()  # Fetch all rows from the result of the query
    cursor.close()  # Close the cursor
    connection.close()  # Close the connection
    return jsonify(rows)  # Return the rows as a JSON response

# Route to get a single user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)  # Use dictionary cursor
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))  # Execute SQL query with parameter
    row = cursor.fetchone()  # Fetch one row
    cursor.close()  # Close the cursor
    connection.close()  # Close the connection
    if row:  # If user is found, return the user as a JSON response
        return jsonify(row)
    return jsonify({'error': 'User not found'}), 404  # If user is not found, return 404 error

# Route to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()  # Get JSON data from the request body
    name = data['name']
    email = data['email']
    password = data['password']
    connection = create_connection()
    cursor = connection.cursor()
    # Execute SQL query to insert new user
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    connection.commit()  # Commit the transaction
    new_id = cursor.lastrowid  # Get the ID of the newly inserted user
    cursor.close()  # Close the cursor
    connection.close()  # Close the connection
    return jsonify({'id': new_id, 'name': name, 'email': email, 'password': password})  # Return the new user as a JSON response

# Route to update an existing user by ID
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()  # Get JSON data from the request body
    name = data['name']
    email = data['email']
    password = data['password']
    connection = create_connection()
    cursor = connection.cursor()
    # Execute SQL query to update the user
    cursor.execute("UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s", (name, email, password, id))
    connection.commit()  # Commit the transaction
    if cursor.rowcount == 0:  # If no rows were affected, the user was not found
        cursor.close()
        connection.close()
        return jsonify({'error': 'User not found'}), 404
    cursor.close()  # Close the cursor
    connection.close()  # Close the connection
    return jsonify({'id': id, 'name': name, 'email': email, 'password': password})  # Return the updated user as a JSON response

# Route to delete a user by ID
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    connection = create_connection()
    cursor = connection.cursor()
    # Execute SQL query to delete the user
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    connection.commit()  # Commit the transaction
    if cursor.rowcount == 0:  # If no rows were affected, the user was not found
        cursor.close()
        connection.close()
        return jsonify({'error': 'User not found'}), 404
    cursor.close()  # Close the cursor
    connection.close()  # Close the connection
    return jsonify({'message': 'User deleted'})  # Return a success message

# Run the Flask application on port 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)
