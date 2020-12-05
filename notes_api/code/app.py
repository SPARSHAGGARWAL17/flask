from resources.users import UserRegister
from resources.notes import Notes, NotesList
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from db import db
app = Flask(__name__)
app.secret_key = 'secret'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)
jwt = JWT(app,authenticate,identity)

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(Notes,'/note')
api.add_resource(UserRegister,'/register')
api.add_resource(NotesList,'/notes/<int:id>')

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000,debug=True)