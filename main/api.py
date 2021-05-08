import requests

class Api:

    def __init__(self):
        pass
    
    def retornaLista(self, url):
        if requests.get(url).status_code == 200:
            lista = requests.get(url)
            return lista.json()
        else:
            return print("Não foi possível capturar a informação da API {}".format(requests.get(url).status_code))
