import sqlite3
class User:
    def __init__(self, _id , name , username):
        self.id = _id
        self.name = name
        self.username = username
    @classmethod
    def find_by_username(cls ,username, password):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
        row = result.fetchone()
        connection.commit()
        connection.close()
        if row:
            return cls(*row)
        else:
            return None
    def find_by_user_id(cls, user_id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM users WHERE id = user_id",(user_id,))
        row = result.fetchone()
        connection.commit()
        connection.close()
        if row:
            return cls(*row)
        else:
            return None
