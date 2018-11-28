from db import db


class UserModel(db.Model):
    '''User Model.'''

    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        '''Save the user in the database.'''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        '''Find a user by username.'''
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        '''Find a user by id.'''
        return cls.query.filter_by(id=_id).first()

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username
