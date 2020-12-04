import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModal

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type = str,
    required = True,
    help = "This field cannot be blank."
    )
    parser.add_argument('password',
    type = str,
    required = True,
    help = "This field cannot be blank."
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModal.find_by_username(data["username"])
        if user:
            return {"message":"user already exists"}
        else:
            user = UserModal(**data)
            user.save_to_db()

        return {"message":"User Created Successfully."}, 201