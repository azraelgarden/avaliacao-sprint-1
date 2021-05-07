#importando pymongo
from pymongo import MongoClient
from api import showUserInfo
from pprint import pprint

user = str(input('Usuário: '))

data_api = showUserInfo(user)
user_info = data_api.return_info()

#conectando 
client = MongoClient("localhost", 27017)

db = client.githubUsers

db.usuarios.insert_one(
    {
        "nome": user_info['login'],
        "avatar": user_info['avatar_url'],
        "perfil": user_info['html_url'],
        "followers": user_info['followers'],
        "following": user_info['following'],
        "public_repositories": user_info['public_repos'],
        "twitter": user_info['twitter_username']
    }
)

for user  in db.usuarios.find():
    pprint(user)
