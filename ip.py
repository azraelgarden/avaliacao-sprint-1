import urllib.request as urllib2
import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.trabalhoAvaliativo

# Caso queira testar algum ip, estes sao válidos
# 24.55.21.33, 2606:4700:10::6816:3866, 15.44.56.9, 43.27.4.8
# 52.211.131.50, 13.94.143.57, 12.53.21.2, 32.12.66.4, 77.54.25.3

def get_ip():
    ip = input("Digite um IP: ")
    response = urllib2.urlopen("http://ipwhois.app/json/{}?lang=pt-BR".format(ip))
    ipgeolocation = json.load(response)
    if ipgeolocation["success"]:
        findone = db.ip.find_one({"ip": ipgeolocation["ip"]})
        if findone:
            print("Este IP ja tem no banco")
            ipgeolocation = findone
            menu(ipgeolocation)
        else:
            print("Adicionando esse ip no banco...")
            db.ip.insert_one(ipgeolocation)
            menu(ipgeolocation)
    else:
        print("Esse IP não é válido! Tente novamente")
        get_ip()

def jaVistos(ipgeolocation):
    print("Aqui estão os IPs já vistos: ")
    for x in db.ip.find({},{"ip"}):
        print(x["ip"])

    escolha = input("Escolha um IP acima ou digite 0 para sair: ")
    if escolha == db.ip.find_one({"ip": escolha}):
        ipgeolocation = db.ip.find_one({"ip": escolha})
        menu(ipgeolocation)
    elif escolha == "0":
        raise SystemExit
    else:
        print("Este IP não está na lista a cima... Tente Novamente")
        jaVistos(ipgeolocation)

def menu(ipgeolocation):
    if False:
        pass
    else:
        opcao = 0
        while opcao != 7:

            print('''-=-=-=-=-=-=-=-=-=-
O que deseja ver sobre ele?
1...Local
2...Dados geograficos
3...Moeda
4...Tudo
5...Novo IP
6...Ips já 
7...Para sair
-=-=-=-=-=-=-=-=-=-'''.format(ipgeolocation["ip"]))
            opcao = int(input("Digite a opção: "))

            if opcao == 1:
                print('''
-=-=-=-=-=-=-=-=-=-
Cidade: {}, Estado: {}, País: {}, Capital: {}, Continente: {},  Bandeira do País: {}
-=-=-=-=-=-=-=-=-=-'''
                      .format(ipgeolocation["city"], ipgeolocation["region"], ipgeolocation["country"],
                              ipgeolocation["country_capital"], ipgeolocation["continent"],ipgeolocation["country_flag"]))

            elif opcao == 2:
                print('''
-=-=-=-=-=-=-=-=-=-            
Latitude: {}, Longitude: {}
-=-=-=-=-=-=-=-=-=-'''
                      .format(ipgeolocation["latitude"], ipgeolocation["longitude"]))

            elif opcao == 3:
                print('''
-=-=-=-=-=-=-=-=-=-
Moeda: {}, Codigo: {}, Símbolo: {}, Plural: {}
-=-=-=-=-=-=-=-=-=-'''
                      .format(ipgeolocation["currency"],
                              ipgeolocation["currency_code"],
                              ipgeolocation["currency_symbol"],
                              ipgeolocation["currency_plural"]))

            elif opcao == 4:
                print('''
-=-=-=-=-=-=-=-=-=-
Cidade: {}, Estado: {}, País: {}, Capital: {},
Latitude: {}, Longitude: {}, Moeda: {}, Codigo: {}, Símbolo: {}, Plural: {}.
-=-=-=-=-=-=-=-=-=-'''
                      .format(ipgeolocation["city"], ipgeolocation["region"], ipgeolocation["country"],
                              ipgeolocation["country_capital"], ipgeolocation["latitude"], ipgeolocation["longitude"],
                              ipgeolocation["currency"], ipgeolocation["currency_code"],
                              ipgeolocation["currency_symbol"],
                              ipgeolocation["currency_plural"]))

            elif opcao == 5:
                get_ip()

            elif opcao == 6:
                jaVistos(ipgeolocation)

            elif opcao == 7:
                print("Saindo...")
                raise SystemExit

            else:
                print('''
-=-=-=-=-=-=-=-=-=-
Opção invalida
-=-=-=-=-=-=-=-=-=-
            ''')

if True:
    get_ip()

