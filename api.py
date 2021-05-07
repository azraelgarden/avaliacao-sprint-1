import requests
import json

class showUserInfo():

    def __init__(self, usuario):
        self._usuario = usuario

    
    def request(self):
        response = requests.get(
            f'https://api.github.com/users/{self._usuario}/repos'
        )
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
    

    def return_repositories(self):
        datas = self.request()
        if type(datas) is not int:
            for i in range(len(datas)):
                print(datas[i]['name'])
        else:
            print(datas)


repositorios = showUserInfo('whoisfreire')
repositorios.return_repositories()
