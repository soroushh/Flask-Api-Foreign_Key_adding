from flask_restful import Resource, Api
from flask import jsonify, request
import sqlite3
from flask_jwt import JWT, jwt_required, current_identity

class Item(Resource):
    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM items WHERE name = ?",(name,))
        connection.commit()
        row = result.fetchone()
        if row:
            connection.close()
            return(jsonify({"name":row[1], "user_id":row[2]}))
        else:
            return {"message": "Item does not exist."}
    @jwt_required()
    def post(self,name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO items VALUES (NULL, ?,?)",(name, current_identity.id))
        connection.commit()
        connection.close()
        return {"message":"Item succesfully was made."}
