#importar as bibliotecas que serao usadas
import requests
import json
import pymongo
from pymongo import MongoClient

#introducao da aplicacao
print()
print("Sou uma Doglover!")
print()
print("Vamos acessar a API publica Dogfacts e trazer alguns fatos interessantes sobre caes!")

#chamada da API
response = requests.get("http://dog-api.kinduff.com/api/facts?number=1") #acessa a api
json_response = response.json() #le e estabelece os dados da api
#armazenado o valor do fato a uma variavel
fatocachorro = json_response['facts']
print()
print("O fato de hoje é:", fatocachorro)
print()
print("Este fato sera adicionado a nossa base!")

#acesso ao banco e a tabela e gravacao da variavel
myclient = MongoClient('localhost', 27017)
mydb = myclient["dogfacts"]
mycol = mydb["facts"]
mydict = { "Fato": fatocachorro }
x = mycol.insert_one(mydict)

print()
print("Todos os fatos que estao na nossa base sao...")
print()

#apresentacao de todos os fatos na tela
mostratudo = mycol.find()
for data in mostratudo:
  print(data)

