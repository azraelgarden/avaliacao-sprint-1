from database import Database
from api import Api

hostname = "mongodb://localhost:27017/"
banco = "spacex"
collection = "rockets"
url = "https://api.spacexdata.com/v4/rockets"

API = Api()
lista = API.retornaLista(url)
db = Database(hostname, banco, collection)
db.inserirVariosRegistros(lista)