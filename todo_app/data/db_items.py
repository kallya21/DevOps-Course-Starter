import pymongo
import os

class Item:
    def __init__(self, _id, name, status = 'To Do'):
        self.id = _id
        self.name = name
        self.status = status

    @classmethod
    def from_db_item(cls, db_item):
        return cls(db_item['_id'], db_item['name'], db_item['status'])
    
def get_primary_connection_string():
    return os.getenv('PRIMARY_CONNECTION_STRING')

def get_mongo_db_name():
    return os.getenv('MONGO_DB_NAME')
    
def get_collection():
    connection_string = get_primary_connection_string()
    client = pymongo.MongoClient(connection_string)
    db_name = get_mongo_db_name()
    db = client[db_name]
    collection = db['todo_items']
    return collection

def get_todo_items():
    collection = get_collection()
    db_items = collection.find({})

    items = []

    for db_item in db_items:
        item = Item.from_db_item(db_item)
        items.append(item)

    return items
    
def add_todo_item(name, status='To Do'):
    collection = get_collection()
    new_item = {'name': name, 'status': status}
    result = collection.insert_one(new_item)
    return result.inserted_id

def update_item_status(item_id, new_status='Done'):
    collection = get_collection()
    result = collection.update_one({'_id': item_id}, {'$set': {'status': new_status}})
    return result.modified_count > 0