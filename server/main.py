from database import Mongobase
from api import showUserInfo

db_name = 'githubUsers'
collection_name = 'users'

user_id = input('digite o usuário: ')

user = showUserInfo(user_id)
user_info = user.response

database = Mongobase(db_name, collection_name)
database.insert(user_info)
database.showAll()
