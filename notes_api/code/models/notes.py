from db import db


class NoteModel(db.Model):
    '''
    Model for creating notes
    '''
    id = db.Column(db.Integer,primary_key= True)
    createdAt = db.Column(db.String(10),nullable = False)
    note = db.Column(db.String(300))

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self,user_id,createdAt,note):
        self.createdAt = createdAt
        self.note = note
        self.user_id = user_id

    def json(self):
        return {"createdAt":self.createdAt,"note":self.note,"user_id":self.user_id,"notes_id":self.id}
    
    @classmethod
    def find_by_user(cls,id):
        return cls.query.filter_by(user_id = id)
    
    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id = id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()