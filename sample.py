# SAMPLE

# Step 1: import SQLite3 Module
import sqlite3

# Step 2: create a connection with a SQL database file
connection = sqlite3.connect("pokemon.db")

# Step 3: create a cursor that helps us to communicate with a the database
cursor = connection.cursor()

# Step 4: execute SQL queries with a method called ".execute()"

result = cursor.execute('''
SELECT * FROM pkmn
''')

print(result)
# print(result.fetchone())
# print(result.fetchall())

for output in result.fetchall():
    print(output)

# Add a value to a certain column
# cursor.execute('''
# UPDATE pkmn
# SET number = 7
# WHERE name = 'Squirtle'
# ''')

# Add a new column
# cursor.execute('''
# ALTER TABLE pkmn
# ADD COLUMN number INTEGER
# ''')

# Create a table
# cursor.execute('''
# CREATE TABLE pkmn (
#     name TEXT,
#     pkmn_type1 TEXT,
#     pkmn_type2 TEXT
# )
# ''')

# Insert a value
# cursor.execute('''
# INSERT INTO pkmn VALUES (
#     'Bulbasaur', 'Grass', 'Poison'
# )
# ''')

# cursor.execute('''
# INSERT INTO pkmn VALUES (
#     'Charmander', 'Fire', NULL
# )
# ''')

# cursor.execute('''
# INSERT INTO pkmn VALUES (
#     'Squirtle', 'Water', NULL
# )
# ''')

# Step 5: Commit Changes & close
connection.commit()

print(f"Current session's number of changes: {connection.total_changes}")

cursor.close()
connection.close()