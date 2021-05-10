import requests
import pymongo
from monta_time import *

pkm_client = pymongo.MongoClient("mongodb://localhost:27017/")
pkm_db = pkm_client["pkm_Team_Database"]
pkm_col = pkm_db["Teams"]

print('Escolha uma opção')

while True:
    option = int(input('1 - Criar Novo Time\n2 - Vizualizar times\n3 - Pokedex\n4 - Sair\n'))
    if option == 1:
        n_time = input('Digite o nome do time: ')
        team_maker = Monta_Time(n_time)
        team_maker.montar()
         

    elif option == 2:
        team_checker = Monta_Time("v1su4l1z4r")
        team_checker.procurar()
        print('\n')
            

    elif option == 3:
        pokedex_checker = Monta_Time("ch3c4g3m")
        pokedex_checker.checar()

    else: 
        print('Saindo....')
        exit()
