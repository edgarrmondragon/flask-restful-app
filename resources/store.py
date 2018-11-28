from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    '''Store Resource.'''
    def get(self, name):
        '''Retrieve a single store by name.'''
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        '''Create a new store.'''
        if StoreModel.find_by_name(name):
            return {
                'message': f'A store with name "{name}" already exists'
            }, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'There was an error inserting the store'}, 500
    
        return store.json(), 201

    def delete(self, name):
        '''Delete a store.'''
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):
    '''Stores resource.'''
    def get(self):
        '''Retrieve a list of stores.'''
        return {'stores': [store.json() for store in StoreModel.query.all()]}
