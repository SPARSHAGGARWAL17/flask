from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from user import UserRegister
from item_list import Item,ItemList
app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret'
api = Api(app)

jwt = JWT(app,authenticate,identity)


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
app.run(port=5000,debug=True)