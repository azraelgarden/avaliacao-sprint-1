from pymongo import MongoClient
from pprint import pprint

class Mongobase:

    def __init__(self, db_name, collection_name):
        self._db = db_name
        self._collection = collection_name
        self.client = MongoClient('localhost', 27017)

        #criando banco
        database = self.client[self._db]

        #criando coleção
        self._collection = database[self._collection]


    def insert(self, user):
        self._collection.insert_one(user)

    def showAll(self):
        for user in self._collection.find():
            pprint(user)