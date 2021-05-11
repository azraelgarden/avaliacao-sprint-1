import pymongo
import requests
#TRATAMENTO DO BANCO DE DADOS
meuCliente = pymongo.MongoClient("mongodb://localhost:27017/")
minhaDatabase = meuCliente["covid-19"]
minhaColecao = minhaDatabase["dino"]


#TRATAMENTO DA API
URL = "https://covid19-brazil-api.vercel.app/api/report/v1?fbclid=IwAR0aJUgRlTxnHkXoVoVzdWaxuoZL1oIrMQaBT4oi8vU91-g4sTfol2dKsKU"
dadosAPI = requests.get(URL)

#INSERE NO BANCO DE DADOS
minhaColecao.insert_one(dadosAPI.json())
