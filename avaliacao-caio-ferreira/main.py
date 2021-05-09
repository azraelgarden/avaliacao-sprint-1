from pymongo import MongoClient
import requests
import json
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

#O mongo por padrão esta conectado na porta 27017
client = MongoClient('localhost', 27017)
db = client.YoutubeResultados

def mostrarResultado(video):
    print('Título: ' + video['TituloDoVideo'])
    print('Descrição: ' + video['Descricao'])
    print('Título do canal: ' + video['Canal'])
    print('Url: https://www.youtube.com/watch?v=' + video['VideoId'])
    print('================================================================================')

pesquisar = str(input('Qual sua pesquisa?: '))

#Checando se no banco de dados existe um chave de cache igual, caso sim
#retorna os itens do banco, caso contrário, busca da API e joga no banco
if db.resultados.count_documents({'CacheKey': pesquisar}) > 0:
    
    print('Essa pesquisa já existe na nossa cache!')
    print('Lista de vídeos encontrados: ')
    resultadoDoBanco = db.resultados.find({'CacheKey': pesquisar})
    
    for item in resultadoDoBanco:
        mostrarResultado(item)
        
else: 
    
    params = {
        'key': config['YOUTUBE_API']['apiKey'], 
        'part': 'snippet', 
        'q': pesquisar,
        'type' : 'video'
    }
    
    request = requests.get(
        config['YOUTUBE_API']['url'], 
        params=params
    ).json()
    
    print('Dados buscado direto da API do Google!')
    print('Lista de vídeos encontrados: ')
    
    for item in request['items']:
        
        video = {
            'CacheKey': pesquisar,
            #Em uma aplicação web pode ser usada a thumbnail
            'Canal' : item['snippet']['channelTitle'],
            'VideoId' : item['id']['videoId'],
            'Thumbnail' : item['snippet']['thumbnails']['default']['url'],
            'TituloDoVideo' : item['snippet']['title'],
            'Descricao' : item['snippet']['description']
        }

        db.resultados.insert_one(video)
        mostrarResultado(video)
        
        