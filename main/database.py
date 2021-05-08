class Databasecontroller:

    def __init__(self, hostname, client, database):
        self.__hostname = hostname
        self.__client = client
        self.__database = database

    def configurar(self):
        import pymongo
        myclient = pymongo.MongoClient(self.__hostname)
        mydb = myclient[self.__client]
        mycol = mydb[self.__database]

