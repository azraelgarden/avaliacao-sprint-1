from database import Database
from api import Api

hostname = "mongodb://localhost:27017/"
banco = "spacex"
collection = "rockets"
url = "https://api.spacexdata.com/v4/rockets"

API = Api()
db = Database(hostname, banco, collection)

lista = API.retornaLista(url)
db.inserirVariosRegistros(lista)