from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message":"store does not exists"}

    def post(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return {"message":"store already exists"}
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message":"Internal server problem"}
        return store.json(),201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message":"Store deleted"}

class StoreList(Resource):
    def get(self):
        return {"stores":[store.json() for store in StoreModel.query.all()]}