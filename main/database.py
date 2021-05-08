import pymongo

class Database:

    def __init__(self, hostname, db):
        self.__hostname = hostname
        self.__db = db
        self.myclient = pymongo.MongoClient(self.__hostname)
    
    def criarCollection(self, collection):
        self.__mycollection = collection
        mydb = self.myclient[self.__db]
        self.__mycollection = mydb[self.__mycollection]
        return self.__mycollection

    def inserirUmRegistro(self, query):
        self.__mycollection.insert_one(query)
    
    def inserirVariosRegistros(self, query):
        self.__mycollection.insert_many(query)
    
    def acharUm(self, query):
        return self.__mycollection.find_one(query)

    def acharUmSemQuery(self):
        return self.__mycollection.find_one({})

    def acharVarios(self, query):
        return self.__mycollection.find(query)
    
    def acharVariosSemQuery(self):
        return self.__mycollection.find({})

    def acharUmPorCollection(self, collection, query):
        return collection.find(query)