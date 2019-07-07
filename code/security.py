from user import User
import sqlite3
def authenticate(username , password):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM users WHERE username=? AND password=? ",(username, password,))
    row = result.fetchone()
    if row:
        user = User(*row)
    else:
        user = None
    connection.close()
    return user

def identify(payload):
    user_id = payload["identity"]
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM users WHERE id=? ",(user_id,))
    row = result.fetchone()
    if row:
        user = User(*row)
    else:
        user = None
    connection.close()
    return user
