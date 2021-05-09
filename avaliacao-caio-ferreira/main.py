#Fazer a importação do MongoClient da lib pymongo
from pymongo import MongoClient
#importar o requests
import requests
#importar o json
import json
from config import apiKey
#O mongo por padrão esta conectado na porta 27017
client = MongoClient('localhost', 27017)
db = client.YoutubeResultados

#Habilitando a chave da API do youtube e armazenando em uma variavel
#A minha chave está armazenada no arquivo config.py, e esse arquivo está sendo ignorado pelo git.
key = apiKey
pesquisar = str(input('Qual sua pesquisa?: '))


resultadoDoBanco = db.resultados.find({'cacheKey': pesquisar})
#Checando se no banco de dados existe um chave de cache igual, caso sim
#retorna os itens do banco, caso contrário, busca da API e joga no banco
if resultadoDoBanco.count() > 0:
    for item in resultadoDoBanco:
        print(item)
        
else: 
    request = requests.get(
        'https://www.googleapis.com/youtube/v3/search', 
        params={'key': key, 'part': 'snippet', 'q': pesquisar}).json()
    for item in request['items']:
        
        db.resultados.insert_many(
            [
                {
                    'cacheKey': pesquisar,
                    'Thumbnail' : item['snippet']['thumbnails']['default']['url'],
                    'TituloDoVideo' : item['snippet']['title'],
                    'Descricao' : item['snippet']['description'],
                    'TituloDoCanal' : item['snippet']['channelTitle']
                        
                }
            ]
        )
        print(item)