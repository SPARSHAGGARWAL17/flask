from models.users import UserModel
from flask_restful import reqparse,Resource

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help='This field is required')
    parser.add_argument('password',type=str,required=True,help='This field is required')

    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data["username"])
        if user:
            return {"message":"user already exist","user_id":user.id}

        user = UserModel(**data)
        user.save_to_db()
        user = UserModel.find_by_username(data["username"])
        return {"message":"user registered successfully","user_id":user.id}