# Imports
import requests
from pymongo import MongoClient
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

# MongoDB e JSON setup
url = "https://omgvamp-hearthstone-v1.p.rapidapi.com/cards"
headers = {
    'x-rapidapi-key': "cd8383753amsh64306410253a513p18dde8jsn2227bef820ed",
    'x-rapidapi-host': "omgvamp-hearthstone-v1.p.rapidapi.com"
}

request = requests.request("GET", url, headers=headers)

js = request.json()

client = MongoClient("localhost", 27017) # TODO Remote MongoDB
name = "hs"
db = client[name]
collection = db[name]
collection.insert_one(js)

hs = collection.find_one()
# Removing useless data
to_remove = ["Basic", "Demo", "System", "Debug", "Promo", "Tavern Brawl", "_id", "Hero Skins"]
for remove in to_remove:
    del hs[remove]

# Organizing keys    
all_expansions = list(hs.keys())
stats = ["cost", "health", "attack"]
all_info = ["Custo das Cartas -> cost", "Vida das criaturas -> health", "Ataque das criaturas -> attack", "Raça das criaturas -> race", "Tipo das cartas -> type", "Facção pertencente -> playerClass", "Raridade -> rarity"]

# Funcs

# Início
def begin():
    print("##############################################")
    print()
    print("Análise exploratória das cartas do Hearthstone")
    print()
    print("##############################################")

    show_expansions()
    show_info()

    choice = str(input("Deseja ver uma Expansão específica ou todas? [E]Específica [T]Todas: ")).upper()
    if choice == 'E':
        choice_one()
    elif choice == 'T':
        choice_global()


# Mostra expansões
def show_expansions():
    print()
    print("Expansões")
    for exp in all_expansions:
        print(exp)

# Mostra info
def show_info():
    print()
    print("Informações")
    for info in all_info:
        print(info)

# Ver todas expansões
def choice_global():
    key_input = str(input("Digite a informação das Expansões que deseja visualizar os dados: ")).lower()
    list_expansion_key = global_list(key_input)
    if key_input in stats:
        print(numpy_statistics(list_expansion_key))
        global_mean_plot(key_input)
    make_bar(list_expansion_key)

# Ver um só
def choice_one():
    expansion_input = str(input("\nInforme a Expansão que deseja visualizar os dados: "))
    key_input = str(input("Digite a informação de uma Expansão que deseja visualizar os dados: ")).lower()
    list_expansion_key = make_list(dict_name=hs, expansion=expansion_input, key_name=key_input)
    if key_input in stats:
        print(numpy_statistics(list_expansion_key))
    make_bar(list_expansion_key)

# Cria lista
def make_list(dict_name, expansion, key_name):
    list_key = []
    for i in range(len(dict_name[expansion])):
        if key_name in dict_name[expansion][i]:
            x = dict_name[expansion][i][key_name]
            list_key.append(x)
        else:
            pass
    return list_key

# Estatísticas da lista
def numpy_statistics(lista):
    minm = np.min(lista)
    maxm = np.max(lista)
    avg = np.mean(lista)
    med = np.median(lista)
    variance = np.var(lista)
    standard = np.std(lista)

    return f"\n\nValor mínimo: {minm}\nValor máximo: {maxm}\nMédia: {avg}\nMediana: {med}\nVariância: {variance}\nDesvio Padrão: {standard}\n\n"

# Gráfico
def make_bar(lista):
    list_counts = Counter(lista)
    g_keys = list(list_counts.keys())
    g_values = list(list_counts.values())

    plt.figure(figsize=(18, 4))
    plt.title("Gráfico Quantidade de aparições X Chave")
    plt.bar(g_keys, g_values)
    plt.show()

# Lista global
def global_list(key_name):
    list_global = []
    for i in hs:
        for j in hs[i]:
            if key_name in j:
                list_global.append(j[key_name])
            else:
                pass
    return list_global

# Gráfico Média global
def global_mean_plot(key_name):
    all_expansions_abv = ["CLA", "HOF", "MIS", "NAX", "GVG", "BLM", "TGT", "CRE", "TLE", "WOG", "ONK", "MSG", "JUG", "KFT", "KEC", "TWW", "TBP",        "RSR", "ROS", "TOT", "SOU", "DOD", "GKA", "AOO", "WEV", "SMA", "BTG", "DHI", "MDF", "FIB", "LGC", "COR", "VNL", "WLC"] 
    list_mean = []
    for i in all_expansions:
        list_aux = make_list(hs, i, key_name)
        x = np.mean(list_aux)
        list_mean.append(x)

    plt.figure(figsize=(15,5))
    plt.title(f"Média da informação {key_name} de todas as expansões na ordem")
    plt.plot(all_expansions_abv, list_mean, color='green', marker='o', linestyle='solid')
    plt.show()

begin()