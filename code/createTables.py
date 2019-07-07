import sqlite3
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)")
cursor.execute("INSERT INTO users VALUES (NULL, 'soroush','khosravi')")
cursor.execute("INSERT INTO users VALUES (NULL, 'farnaz', 'ostovari')")
cursor.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, user_id INTEGER ,FOREIGN KEY(user_id) REFERENCES user(id))")
connection.commit()
connection.close()
