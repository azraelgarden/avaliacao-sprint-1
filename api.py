import requests
import json

class showUserInfo():

    def __init__(self, usuario):
        self._usuario = usuario

    
    def __request(self):
        response = requests.get(
            f'https://api.github.com/users/{self._usuario}'
        )
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
    

    @property
    def show_info(self):
        print(self.__request())


    def return_info(self):
        return self.__request()
        
