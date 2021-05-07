#importando pymongo
from pymongo import MongoClient
from api import showUserInfo

data_api = showUserInfo('whoisfreire')
user = data_api.return_info()
#conectando 
client = MongoClient("localhost", 27017)

db = client.githubUsers

db.usuarios.insert_one(
    {
        "nome": user['login'],
        "avatar": user['avatar_url'],
        "perfil": user['html_url'],
        "followers": user['followers'],
        "following": user['following'],
        "public_repositories": user['public_repos'],
        "twitter": user['twitter_username']
    }
)
