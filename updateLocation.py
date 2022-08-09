import random
from pymongo import MongoClient
import datetime

def random_location():
    x_lad = random.uniform(28.55195,28.75195)
    y_long = random.uniform(77.13149,77.33149)
    return [x_lad,y_long]
        
#database
db_uri = 'mongodb://localhost:27017'
mongo_connect = MongoClient(db_uri)

db = mongo_connect.taxi_customer_db
taxi_col = db.taxis

for obj in taxi_col.find():
    taxi_col.update_one({'id':obj['id']}, {'$set':{'timestamp':datetime.datetime.now()}})
    taxi_col.update_one({'id':obj['id']}, {'$set':{'location':{'coordinates':random_location()}}})
    print('updating ...')


