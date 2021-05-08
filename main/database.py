import pymongo

class Database:

    def __init__(self, hostname, db, collection):
        self.__hostname = hostname
        self.__db = db
        self.__mycollection = collection
        self.myclient = pymongo.MongoClient(self.__hostname)
        mydb = self.myclient[self.__db]
        self.__mycollection = mydb[self.__mycollection]

    def inserirVariosRegistros(self, query):
        self.__mycollection.insert_many(query)
