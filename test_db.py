import sqlite3

# Connect to the existing database
conn = sqlite3.connect('Herguide.db')
cursor = conn.cursor()

# Show all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print("-", table[0])

conn.close()
