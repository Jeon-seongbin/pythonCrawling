from pymongo import MongoClient

class InsertMongoDb:
    client = 0
    db = 0
    price = 0

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["price"]
        self.price = self.db.price

    def insertData(self, insertData):
        for data in insertData:
            self.price.insert_one(data).inserted_id
