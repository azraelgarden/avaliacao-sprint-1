import urllib.request as urllib2
import json

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.trabalhoAvaliativo


# Caso queira testar alguns ips, esses sao validos
# 24.55.21.33, 2606:4700:10::6816:3866
# 52.211.131.50, 13.94.143.57

def get_ip():
    ip = input("Digite um IP: ")
    response = urllib2.urlopen("http://ipwhois.app/json/" + ip)
    ipgeolocation = json.load(response)

    if ipgeolocation["success"]:
        findone = db.ip.find_one({"ip": ipgeolocation["ip"]})
        if findone:
            print("ja tem no banco")
            ipgeolocation = findone
            menu(ipgeolocation)
        else:
            print("nao tinha no banco")
            db.ip.insert_one(ipgeolocation)
            menu(ipgeolocation)
    else:
        print("Esse IP não é válido! Tente novamente")
        get_ip()

def historicoIP(ipgeolocation):

    contador = 1
    historico= []
    while contador != 0:
        historico = [ipgeolocation["ip"]]
        print(historico)
        get_ip()
    pass

def menu(ipgeolocation):
    if False:
        pass
    else:
        opcao = 0
        while opcao != 7:

            print('''O IP {} é válido, O que deseja ver sobre ele?
1...Local
2...Dados geograficos
3...Moeda
4...Tudo
5...Novo IP
6...Historico de buscas de IP
7...Para sair
-=-=-=-=-=-=-=-=-=-'''.format(ipgeolocation["ip"]))
            opcao = int(input("Digite a opção: "))

            if opcao == 1:
                print('''
-=-=-=-=-=-=-=-=-=-
Cidade: {}, Estado: {}, País: {}, Capital: {}
-=-=-=-=-=-=-=-=-=-'''
                      .format(ipgeolocation["city"], ipgeolocation["region"], ipgeolocation["country"],
                              ipgeolocation["country_capital"]))

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
                historicoIP(ipgeolocation)
                #get_ip()


            elif opcao == 7:
                print("Saindo...")
                return False

            else:
                print('''
-=-=-=-=-=-=-=-=-=-
Opção invalida
-=-=-=-=-=-=-=-=-=-
            ''')


if True:
    get_ip()

