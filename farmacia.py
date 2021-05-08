import pymongo
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["farmaciadbdb"]
mycol = mydb["farmaciadbtable"]

URL = "https://sage.saude.gov.br/paineis/farmaciaPopular/lista_farmacia.php?output=json"

response = requests.get(URL)
print(response.json())

x = mycol.insert_one(response.json())