import sqlite3
import pandas as pd

# Load the Excel file
excel_file = "ApartmentLIst.xlsx"

# If the data is on a specific sheet, specify it with sheet_name
df = pd.read_excel(excel_file, sheet_name="Data")

# Convert each row to a list
list_of_rows = [row.values.tolist() for _, row in df.iterrows()]

# Clean the data: remove trailing spaces
list_of_rows_cleaned = [[
    item[0].strip(),   # Remove trailing spaces from NAME
    item[1].strip(),   # Remove trailing spaces from ADDRESS
    item[2],           # No cleaning needed for MINIMUM
    item[3],           # No cleaning needed for MAXIMUM
    item[4],           # No cleaning needed for NUMBERS
    item[5].strip()    # Remove trailing spaces from SITES
] for item in list_of_rows]

# Connect to the SQLite database (will create if not exists)
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object
cursor = conn.cursor()

for row in list_of_rows_cleaned:
    name, address, minimum, maximum, phone, website = row[0], row[1], row[2], row[3], row[4], row[5]
    sql_queries = [
        f"INSERT INTO APARTMENTS (NAME) VALUES ('{name}')",
        f"INSERT INTO ADDRESSES (ADDRESS, APTID) VALUES ('{address}', (SELECT APTID FROM APARTMENTS ORDER BY APTID DESC LIMIT 1))",
        f"INSERT INTO AMOUNTS (MINIMUM, MAXIMUM, APTID) VALUES ({minimum}, {maximum}, (SELECT APTID FROM APARTMENTS ORDER BY APTID DESC LIMIT 1))",
        f"INSERT INTO CONTACTS (PHONE, WEBSITE, APTID) VALUES ('{phone}', '{website}', (SELECT APTID FROM APARTMENTS ORDER BY APTID DESC LIMIT 1))"
    ]
    for query in sql_queries:
        cursor.execute(query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()