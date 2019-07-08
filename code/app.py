import os
from flask import Flask
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required
from user import User
from item import Item, ItemList, MyItems
from security import authenticate, identify
app = Flask(__name__)
api = Api(app)
app.secret_key = os.environ["SECRET_KEY"]
jwt = JWT(app, authenticate, identify)
api.add_resource(Item , "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(MyItems , '/myItems')
if "__main__" == __name__:
    app.run(port = 5000, debug = True)
