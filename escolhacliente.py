import requests
import pymongo
from apicorreios import *

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

try:
    print(RED + "Bem vindo ao sistema de busca de cep! \n" + RESET)
    nome = input('Digite seu nome ? ')
    visualizarBusca = BuscandoCep(nome)
    visualizarBusca.localizarcep()
except:
        print(f'O cep não consta em nossa base de consulta!')
        print(RED + "XXXXXXXXXXXXXXXXXXXXXXXXX BUSCA CEP XXXXXXXXXXXXXXXXXXXXXXXXX" + RESET)