from flask import Flask
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required
from user import User
from item import Item
# from person import Person
from security import authenticate, identify
app = Flask(__name__)
api = Api(app)
app.secret_key = "soroush"
jwt = JWT(app, authenticate, identify)
api.add_resource(Item , "/item/<string:name>")
if "__main__" == __name__:
    app.run(port = 5000, debug = True)
