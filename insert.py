from pymongo import MongoClient

class InsertMongoDb:
    client = 0
    db = 0
    price = 0

    def __init__(self):
        InsertMongoDb.client = MongoClient('localhost', 27017)
        InsertMongoDb.db = InsertMongoDb.client["price"]
        InsertMongoDb.price = InsertMongoDb.db.price

    def insertData(self, insertData):
        for data in insertData:
            InsertMongoDb.price.insert_one(data).inserted_id

