import requests
import pymongo

pkm_client = pymongo.MongoClient("mongodb://localhost:27017/")
pkm_db = pkm_client["pkm_Team_Database"]
pkm_col = pkm_db["Teams"]

class Monta_Time:

    def __init__(self, nome, pkm_name = 'missingNo'):
        self.nome = nome
        self.pkm_name = 'missingNo'
 
    def checar(self):
        pkm_id = input('Digite o nome ou numero do pokemon: ').lower()
        pokemon_info = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pkm_id}/')
        pkm_validar = str(pokemon_info)

        if pkm_validar == '<Response [200]>':
            pkm_info = pokemon_info.json()
        else:
            print('Nome Errado/Numero Invalido, por favor insira um nome/numero valido')
            self.checar()
        
        self.pkm_name = pkm_info["name"]

        print(f'nome: {self.pkm_name}')
        print(f'numero: {pkm_info["id"]}')
        print(f'tipo: {pkm_info["types"]}')
            
        
        
    def add_pkm(self, time_pkm):
        self.checar()
        option = int(input('Deseja adicionar este pokemon ao time? \n  1 - Sim\n  2 - Escolher novamente\n'))
        if option == 1:
            time_pkm.append(self.pkm_name)
        else: 
            self.add_pkm(time_pkm)

    def montar(self):
        time_pkm = []
        x = range(6)
        for i in x:
            self.add_pkm(time_pkm)
            option = int(input('Deseja adicionar outro pokemon ao time? \n  1 - Sim\n  2 - Não\n'))
            if option == 2:
                break
              
        print(self.nome, ':' ,time_pkm)
        pkm_dict = {"nome": self.nome, "time": time_pkm}
        pkm_col.insert_one(pkm_dict)
        print('Time inserido com sucesso!!!')   

    def procurar(self):
        print('Escolha uma opção: ')
        option = int(input('1 - Vizualizar todos\n2 - Vizualizar um\n3 - Voltar\n'))
        if option == 1:
            print('Checando...')
            for x in pkm_col.find():
                print(x)
        elif option == 2:
            name_check = input('Digite o nome do time desejado: ')
            print('Checando...')
            name_query = {'nome' : name_check}
            team_search = pkm_col.find(name_query)
            for x in team_search:
                print(x)