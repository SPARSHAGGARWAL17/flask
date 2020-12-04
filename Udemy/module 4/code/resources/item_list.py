from models.item import ItemModel
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from flask import request
import sqlite3

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help='This cannot be empty')
    parser.add_argument('store_id',type=int,required=True,help='This cannot be empty')
    @jwt_required()
    def get(self,name):
        id = request.args.get('id',type=int,default=1)
        item = ItemModel.find_by_name(name,id)
        if item:
            return item.json()
        return {"message":"Item not found"},404

    def post(self,name):
        id :int = request.args.get('id',type=int)
        item = ItemModel.find_by_name(name,id)
        print(id)
        if id is None:
            return {"message":"invalid id"}
        if item:
            return {"message":"Item already exists"}
        data = Item.parser.parse_args()
        item = ItemModel(name,**data)
        try:
            item.save_to_db()
        except:
            return {"message":"Internal server error occurred"}
        return item.json(), 201

    def delete(self,name):
        id = request.args.get('id',type=int)
        item = ItemModel.find_by_name(name,id)
        if item:
            item.delete_from_db()
            return {"message":"Item deleted"}
        return {"message":"Item not found"}
    
    def put(self,name):
        data =   Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data["price"]
        else:
            item = ItemModel(name,**data)
        
        item.save_to_db()
        return item.json()

class ItemList(Resource):
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all()]} , 200