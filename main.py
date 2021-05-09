import pymongo
import requests
import webbrowser
from pymongo import MongoClient


# Pymongo
client = pymongo.MongoClient('localhost', 27017)

digidb = client["digidb"]
digicol = digidb["digilink"]


# verificando conexão com API
res = requests.get('https://digimon-api.vercel.app/api/digimon')
print(f'Codigo HTTP da API é: {res.status_code}')
if res:
    print("Não existe erros HTTP\n")
else:
    print("Existe um erro HTTP")


while True:
    print("#####################################################################################")
    print("##                               Searchmon                                         ##")
    print("############  Escreva o nome de um digimon para ver sua foto  #######################")
    print("#####################################################################################")
    print("########################## Digite quit para sair ####################################")
    name = input("Digite o nome do digimon: ").lower()
    if name == 'quit':
        print("Fechando")
        break

    img_url = 'https://digimon.shadowsmith.com/img/'
    #name = 'agumon'
    name_search = img_url + name.lower() + '.jpg'  ## ------------------prepara busca de foto por nome
    webbrowser.open(name_search)  ## -----------------------------------busca imagem do digimon especificado
    print("O link da imagem foi salvo no digilink dentro do digidb usando Pymongo")
    digimon = {"nome": name, "img link": name_search}
    digicol.insert_one(digimon)
