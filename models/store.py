from db import db


class StoreModel(db.Model):
    '''Store model'''
    __tablename__ = 'stores'

    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'name': self.name,
            'items': [item.json() for item in self.items.all()]
        }

    @classmethod
    def find_by_name(cls, name):
        '''Find a single store by name.'''
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        '''Upsert a store in the database.'''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        '''Delete a store from the database.'''
        db.session.delete(self)
        db.session.commit()
