customer_list = [
                {
                    'name': "Mohan",
                    'location': {
                        'type': "Point",
                        'coordinates': [28.64454, 77.23098]
                    }
                },
                {
                    'name': "Isaac",
                    'location': {
                        'type': "Point",
                        'coordinates': [28.67676, 77.23156]
                    }
                },
                {
                    'name': "Amir",
                    'location': {
                        'type': "Point",
                        'coordinates': [28.65213, 77.23121]
                    }
                },
                {
                    'name': "Ashok",
                    'location': {
                        'type': "Point",
                        'coordinates': [28.66132, 77.23176]
                    }
                },
                {
                    'name': "Leonard",
                    'location': {
                        'type': "Point",
                        'coordinates': [28.67423, 77.23172]
                    }
                }
            ]
## extra just on local machine
from pymongo import MongoClient
import pprint
import datetime

ts = datetime.datetime.now()
loop = 0
for i in customer_list:
    loop += 1
    i['timestamp'] = ts
    i['id'] = loop


db_uri = 'mongodb://localhost:27017'
mongo_connect = MongoClient(db_uri)

## creating Database
db = mongo_connect["taxi_customer_db"]

## creating taxi collection
customer = db["customers"]
res = customer.delete_many({})

# Populate the Collections
res = customer.insert_many(customer_list)

# for doc in taxis.find():
#     pprint.pprint(doc)