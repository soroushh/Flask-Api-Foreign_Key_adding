from flask_restful import Resource
from flask_jwt import jwt_required
class Person(Resource):
    @jwt_required()
    def get(self):
        return {"message":"You are able to do authentication now."}
