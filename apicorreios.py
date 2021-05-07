import urllib.request as consulta #chamei uma biblioteca urllib
import json #chamei um json
from pymongo import MongoClient
from flask import Flask, render_template
from flask import make_response

cliente = MongoClient('localhost', 27017)

# print(cliente.list_database_names()) # consultando se está conectado no banco

banco = cliente['test'] #buscando o nome do banco
buscacep = banco["buscacep"] # buscando a tebale do banco

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"


print(RED + "Bem vindo ao sistema de busca de cep!" + RESET)


nome = input('Digite seu nome ? ')
cep = int(input("Digite seu cep ex: 12345678 ? "))

try:
    resultadocep = cep
    site = 'https://viacep.com.br/ws/%s/json/' % resultadocep
    cabecalho = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'} #usei o user agente do meu
    requisicao = consulta.Request(site, headers=cabecalho, method='GET') # usei a urllib.request 
    cliente = consulta.urlopen(requisicao) #Abrindo a url
    retornoconsulta = cliente.read().decode('utf-8')
    cliente.close()
    # print(retornoconsulta) # retornoando os dados JSON

    endereco = json.loads(retornoconsulta) #lendo o resultado JSON
    # print(endereco) exibinido o resultado

    if endereco == {'erro': True}: #se o resultado vir erro o cep está invalido
      print(f'O cep {cep} não consulta em nossa base de consulta!')
    else:
      numero = int(input("Digite o numero do seu endereço ? "))
      complemento = input("Digite o complemento ex: Casa/Aprt ? ")
      referencia = input("Digite a referência do seu endereço ex: Esquina/Loja ? ")

      print(f'Ola {nome} segue o seu endereço: ')
      print('Endereço: ', endereco['logradouro'])
      print(f'Numero: {numero}')
      print(f'Complemento: {complemento}')
      print(f'Referência: {referencia}')
      print('Bairro: ', endereco['bairro'])
      print('Cidade: ', endereco['localidade'])
      print('Estado: ', endereco['uf'])  

      gravando = input('Deseja cadastrar o seus dados ex: sim/nao ? ')

      if gravando == 'sim':
        dados = {
          "Nome:": nome,
          "Endereço:": endereco['logradouro'],
          "Numero:": numero,
          "Complemento:": complemento,
          "Referência:": referencia,
          "Bairro:": endereco['bairro'],
          "Cidade:": endereco['localidade'],
          "Estado:": endereco['uf'],
          }
        dadosgravado = buscacep.insert_one(dados)

        print(f'Obrigado {nome} por cadastrar seu dados em nosso sitemas!.... \n\n\n')
        print(RED + "XXXXXXXXXXXXXXXXXXXXXXXXX BUSCA CEP XXXXXXXXXXXXXXXXXXXXXXXXX" + RESET)
      else:
        print(f'Até logo {nome} por usar nosso sitema seus dados não foram cadastrados \n\n\n')        
        print(RED + "XXXXXXXXXXXXXXXXXXXXXXXXX BUSCA CEP XXXXXXXXXXXXXXXXXXXXXXXXX" + RESET)
      
    app = Flask(__name__)

    @app.route("/")
    def json_api():
      pessoas = [
        {"Nome": nome},
        {"Endereço": endereco['logradouro'] + "<br>"},
        {"Numero": numero},
        {"Complemento": complemento},
        {"Referência": referencia},        
        {"Bairro": endereco['bairro']},
        {"Cidade": endereco['localidade']},
        {"Estado": endereco['uf']},
        ]
      response = make_response(json.dumps(pessoas))
      response.content_type = "application/json"
      return response
    @app.route("/resultado")
    def retornohtml():
      return (f"<h1> Buscando CEP </h1> <hr> <br> <h3> Nome: {nome} <br> Endereço: {endereco['logradouro']} <br> Numero: {numero} <br> Complemento: {complemento} <br> Referência: {referencia} <br> Bairro: {endereco['bairro']} <br> Cidade: {endereco['localidade']} <br> Estado: {endereco['uf']} <br> </h3>")

      print(RED + "http://127.0.0.1:5000/resultado" + RESET)
    app.run()
        

except:
  print(f'Por favor Digite um cep valido, o cep {cep} está invalido!')
  print(RED + "XXXXXXXXXXXXXXXXXXXXXXXXX BUSCA CEP XXXXXXXXXXXXXXXXXXXXXXXXX" + RESET)



