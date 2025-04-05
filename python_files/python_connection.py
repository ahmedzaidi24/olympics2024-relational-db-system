import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        # Establish the connection
        conn = mysql.connector.connect(
            host="localhost",       
            user="dsuser",          
            password="userCreateSQL", 
            database="zaidisyed_20972008" 
        )
        
        # To Check if the connection was successful
        if conn.is_connected():
            print("Python connected to MySQL")
            print(f"Connected to database: {conn.database}")
            return conn  # Return the connection object

    except Error as e:
        print(f"Error: {e}")
        return None

# Create the connection when this file is run or imported
connection = create_connection()

