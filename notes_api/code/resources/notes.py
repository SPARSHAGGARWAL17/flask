from flask_jwt import jwt_required
from models.notes import NoteModel
from flask_restful import Resource,reqparse
from datetime import datetime


class Notes(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id',type=int,required=True,help='This field is required')
    parser.add_argument('createdAt',type=str,required=True,help='This field is required')
    parser.add_argument('note',type=str,required=True,help='This field is required')

    @jwt_required()
    def get(self,id):
        note = NoteModel.find_by_id(id)
        if note:
            return note.json()
        else:
            return {"message":"note not found"}

    @jwt_required()
    def post(self):
        data = Notes.parser.parse_args()
        try:
            print(datetime(*tuple(map(int,data["createdAt"].split('-')))))
        except Exception as e:
            return {"error":f'{e}'}
        note = NoteModel(**data)
        try:
            note.save_to_db()
            return note.json()
        except:
            return {"message":"Internal Error Occurred"}


class NotesList(Resource):
    @jwt_required()
    def get(self,id):
        note = NoteModel.find_by_user(id)
        notes = []
        for i in note:
            notes.append(i.json())
        return{"notes":notes}
