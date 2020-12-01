from flask import Flask, request, make_response
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret'
api = Api(app)

jwt = JWT(app,authenticate,identity)

items = []

class Item(Resource):
    @jwt_required()
    def get(self,name):
        print(name)
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item':item}, 200 if item else 404

    def post(self,name):
        if next(filter(lambda x: x['name'] == name, items),None) is not None:
            return {'message':f"An item with name {name} already exists."}, 400
        data = request.get_json(silent = True)
        item = {'name':name,'price':data['price']}
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items = list(filter(lambda x:x["name"] != name, items))
        return {"message":"item deleted"}
    
    def put(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'price',
            type=float,
            required = True,
            help = 'This field is required',
        )
        data = parser.parse_args()

        item = next(filter(lambda x: x["name"] == name,items),None)
        if item is None:
            item = {"name":name,"price":data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return {'items':items} , 200

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
app.run(port=5000,debug=True)