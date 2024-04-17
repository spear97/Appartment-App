import sqlite3

def get_all_apartment_data():
    
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SELECT statement
    cursor.execute("SELECT NAME FROM APARTMENTS")

    # Fetch all rows
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()