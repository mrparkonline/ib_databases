# Python + SQLite Lesson 3

# Step 1: import SQLite3 Module
import sqlite3

# Step 2: create a connection with a SQL database file
connection = sqlite3.connect("spicy.db")

# Step 3: create a cursor that helps us to communicate with a the database
cursor = connection.cursor()

# Step 4: execute SQL queries with a method called ".execute()" from the cursor

# QUERIES GO HERE

# Step 5: when finished with the database, close your cursor and connection
cursor.close()
connection.close()