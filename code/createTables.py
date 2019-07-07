import sqlite3
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)")
cursor.execute("INSERT INTO users VALUES (NULL, 'soroush','khosravi')")
cursor.execute("INSERT INTO users VALUES (NULL, 'farnaz', 'ostovari')")
connection.commit()
connection.close()
