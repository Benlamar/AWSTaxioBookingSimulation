import random
from pymongo import MongoClient
import datetime, json
import requests

def random_location():
    x_lad = random.uniform(28.55195,28.75195)
    y_long = random.uniform(77.13149,77.33149)
    return [x_lad,y_long]
        
#database
db_uri = 'mongodb://localhost:27017'
mongo_connect = MongoClient(db_uri)

db = mongo_connect.taxi_customer_db
customer_col = db.customers

# for obj in customer_col.find():
#     customer_col.update_one({'id':obj['id']}, {'$set':{'timestamp':datetime.datetime.now()}})
#     customer_col.update_one({'id':obj['id']}, {'$set':{'location':{'type':'Point','coordinates':random_location()}}})
    
#     print('updating ...')

id = random.randint(1,5)
customer_col.update_one({'id':id}, {'$set':{'location':{'type':'Point','coordinates':random_location()}}})

name ='alex'
url = 'http://localhost:8080/alex/search'
myobj = {"source": str({
            "type": "Point",
            "coordinates": [28.67676, 77.23156]
            }),
        "destination":"Assam"}

x = requests.post(url, data = myobj)

print(x.text)