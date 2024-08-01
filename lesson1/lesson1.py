# Python + SQLite Lesson 1

# Step 1: import SQLite3 Module
import sqlite3

# Step 2: create a connection with a SQL database file
connection = sqlite3.connect("pokemon.db")

# Step 3: create a cursor that helps us to communicate with a the database
cursor = connection.cursor()

# Step 4: execute SQL queries with a method called ".execute()" from the cursor

# QUERIES GO HERE


# Step 5: Commit your changes on the database
connection.commit()

# Step 6: Optional, see the total number of changes
print(f"Current Session's Number of changes: {connection.total_changes}")

# Step 7: When finished with the database, close your connection
connection.close()
