import urllib.request as consulta  # chamei uma biblioteca urllib
import json  # chamei um json
from pymongo import MongoClient
from flask import Flask, render_template
from flask import make_response
from sys import exit

cliente = MongoClient('localhost', 27017)

# print(cliente.list_database_names()) # consultando se está conectado no banco

banco = cliente['test']  # buscando o nome do banco
buscacep = banco["buscacep"]  # buscando a tebale do banco

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


class BuscandoCep:
    def __init__(self, nome):
        self.__nome = nome

    def localizarcep(self):
        cep = int(input("Digite seu cep ex: 12345678 ? "))
        resultadocep = cep
        site = 'https://viacep.com.br/ws/%s/json/' % resultadocep
        # usei o user agente do meu
        cabecalho = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        requisicao = consulta.Request(
            site, headers=cabecalho, method='GET')  # usei a urllib.request
        cliente = consulta.urlopen(requisicao)  # Abrindo a url
        retornoconsulta = cliente.read().decode('utf-8')
        cliente.close()
        # print(retornoconsulta) # retornoando os dados JSON

        endereco = json.loads(retornoconsulta)  # lendo o resultado JSON
        # print(endereco)  # exibinido o resultado

        if endereco == {'erro': True}:  # se o resultado vir erro o cep está invalido
            print(
                f'O cep {resultadocep} não consta em nossa base de consulta!')
            exit()
        else:
            numero = int(input("Digite o numero do seu endereço ? "))
            complemento = input("Digite o complemento ex: Casa/Aprt ? ")
            referencia = input(
                "Digite a referência do seu endereço ex: Esquina/Loja ? ")

            print(f'Ola {self.__nome} segue o seu endereço: ')
            print('Endereço: ', endereco['logradouro'])
            print(f'Numero: {numero}')
            print(f'Complemento: {complemento}')
            print(f'Referência: {referencia}')
            print('Bairro: ', endereco['bairro'])
            print('Cidade: ', endereco['localidade'])
            print('Estado: ', endereco['uf'])

            gravando = input(
                'Deseja cadastrar o seus dados ex: sim/nao ? ')

            if gravando == 'sim':
                dados = {
                    "Nome:": self.__nome,
                    "Endereço:": endereco['logradouro'],
                    "Numero:": numero,
                    "Complemento:": complemento,
                    "Referência:": referencia,
                    "Bairro:": endereco['bairro'],
                    "Cidade:": endereco['localidade'],
                    "Estado:": endereco['uf'],
                }
                dadosgravado = buscacep.insert_one(dados)

                print(
                    f'Obrigado {self.__nome} por cadastrar seu dados em nosso sitemas!.... \n\n\n')
                print(
                    RED + "XXXXXXXXXXXXXXXXXXXXXXXXX BUSCA CEP XXXXXXXXXXXXXXXXXXXXXXXXX" + RESET)
            else:
                print(
                    f'Até logo {self.__nome} por usar nosso sitema seus dados não foram cadastrados \n\n\n')
                print(
                    RED + "XXXXXXXXXXXXXXXXXXXXXXXXX BUSCA CEP XXXXXXXXXXXXXXXXXXXXXXXXX" + RESET)

        app = Flask(__name__)

        @app.route("/json")
        def json_api():
            pessoas = [
                {"Nome": self.__nome},
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

        @app.route("/")
        def retornohtml():
            return (f"<h1> Buscando CEP </h1> <hr> <br> <h3> Nome: {self.__nome} <br> Endereço: {endereco['logradouro']} <br> Numero: {numero} <br> Complemento: {complemento} <br> Referência: {referencia} <br> Bairro: {endereco['bairro']} <br> Cidade: {endereco['localidade']} <br> Estado: {endereco['uf']} <br> </h3> <a href='http://127.0.0.1:5000/json'>JSON</a>")
            print(RED + "http://127.0.0.1:5000/resultado" + RESET)
        app.run()
