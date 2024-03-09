import psycopg2
from psycopg2 import OperationalError

# Replace with your actual database connection details
connection_params = {
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'Food_app',
    'user': 'postgres',
    'password': '12345',
}

# Replace with the actual registration data
registration_data = {
    'firstname': 'John',
    'lastname': 'Doe',
    'email': 'john.doe@example.com',
    'phonenumber': '1234567890',
    'gender': 'Male',
    'username': 'john_doe',
    'password': 'secure_password',
}

try:
    # Establish a connection to the PostgreSQL server
    connection = psycopg2.connect(**connection_params)

    # If the connection is successful, print a success message
    print("Connected to the PostgreSQL database!")

    # Create a cursor object for executing SQL queries
    cursor = connection.cursor()

    # Example: Create the 'users' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            firstname VARCHAR(255) NOT NULL,
            lastname VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phonenumber VARCHAR(20) NOT NULL,
            gender VARCHAR(10) NOT NULL,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        );
    """)

    # Commit the table creation
    connection.commit()

    # Example: Insert user registration data into the 'users' table
    cursor.execute("""
        INSERT INTO users(firstname, lastname, email, phonenumber, gender, username, password) 
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (
        registration_data['firstname'],
        registration_data['lastname'],
        registration_data['email'],
        registration_data['phonenumber'],
        registration_data['gender'],
        registration_data['username'],
        registration_data['password']
    ))

    # Commit the changes to the database
    connection.commit()

    # Print a success message
    print("User registration successful!")

except OperationalError as e:
    # If an exception occurs, print an error message
    print(f"Error connecting to the PostgreSQL database: {e}")

finally:
    # Close the cursor and connection in the 'finally' block
    if 'connection' in locals():
        cursor.close()
        connection.close()
        print("Connection closed.")
