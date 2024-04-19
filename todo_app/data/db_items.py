import pymongo
import os

class Item:
    def __init__(self, name, status = 'To Do'):
        self.name = name
        self.status = status

    @classmethod
    def from_db_item(cls, db_item):
        return cls(db_item['name'], db_item['status'])
    
def get_mongo_client():
    connection_string = os.getenv('PRIMARY_CONNECTION_STRING')
    client = pymongo.MongoClient(connection_string)
    return client

def get_todo_items():
    client = get_mongo_client()
    db_name = os.getenv('MONGO_DB_NAME')
    db = client[db_name]
    collection = db['todo_items']
    items = collection.find({})
    return items
    
def add_todo_item(name, status='To Do'):
    client = get_mongo_client()
    db_name = os.getenv('MONGO_DB_NAME')
    db = client[db_name]
    collection = db['todo_items']
    new_item = {'name': name, 'status': status}
    result = collection.insert_one(new_item)
    return result.inserted_id

def update_item_status(item_id, new_status='Done'):
    client = get_mongo_client()
    db_name = os.getenv('MONGO_DB_NAME')
    db = client[db_name]
    collection = db['todo_items']
    result = collection.update_one({'_id': item_id}, {'$set': {'status': new_status}})
    return result.modified_count > 0