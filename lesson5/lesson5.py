# Python + SQLite Lesson 5

# Step 1: import SQLite3 Module
import sqlite3

# Step 2: create a connection with a SQL database file
connection = sqlite3.connect("orders.db")

# Step 3: create a cursor that helps us to communicate with a the database
cursor = connection.cursor()

# Step 4: execute SQL queries with a method called ".execute()" from the cursor

# QUERIES GO HERE

q1 = """
SELECT COUNT(DISTINCT CustomerID) FROM Orders
"""

cursor.execute(q1)
rows = cursor.fetchall()

for row in rows:
    print(row)

attribute_names = [description[0] for description in cursor.description]
print("Attribute names in the Orders table:", attribute_names)

# END OF QUERIES
# Step 5: when finished with the database, close your cursor and connection
cursor.close()
connection.close()