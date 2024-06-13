// Import necessary packages
import express from "express";
import mysql from "mysql2/promise";

// Initialize the Express application
const app = express();
const port = 3000; // Define the port on which the server will listen

// Create a MySQL connection pool
const pool = mysql.createPool({
  host: "localhost", // The hostname of the database you are connecting to
  user: "root", // Your MySQL username
  password: "", // Your MySQL password (replace with your actual password)
  database: "user_management", // The name of the database to use
  waitForConnections: true, // Wait for connections when the pool is full
  connectionLimit: 10, // The maximum number of connections in the pool
  maxIdle: 10, // The maximum number of idle connections in the pool
  idleTimeout: 60000, // The idle timeout for connections (in milliseconds)
  queueLimit: 0, // The maximum number of queued connection requests (0 means no limit)
  enableKeepAlive: true, // Enable TCP Keep-Alive on the connection
  keepAliveInitialDelay: 0, // The initial delay before TCP Keep-Alive packets are sent (in milliseconds)
});

// Define a route to handle GET requests for fetching all users
app.get("/users", async (req, res) => {
  try {
    // Execute a query to select all users from the 'users' table
    const [rows] = await pool.query("SELECT * FROM users");
    // Send the result as a JSON response
    res.json(rows);
  } catch (err) {
    // If an error occurs, send a 500 status and the error message as JSON
    res.status(500).json({ error: err.message });
  }
});

// Start the Express server and listen on the specified port
app.listen(port, () => {
  console.log(`Server running on port ${port}`); // Log a message to indicate the server is running
});
