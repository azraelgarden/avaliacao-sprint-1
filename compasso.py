import pymongo
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["coviddb"]
mycol = mydb["covidtable"]

URL = "https://api.covid19api.com/country/brazil"

response = requests.get(URL)
print(response.json())

x = mycol.insert_many(response.json())
