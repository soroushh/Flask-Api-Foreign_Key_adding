from user import User
import sqlite3
def authenticate(username , password):
    return User.find_by_username(username , password)

def identify(payload):
    user_id = payload["identity"]
    return User.find_by_user_id(user_id)
