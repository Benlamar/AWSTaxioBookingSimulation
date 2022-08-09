from flask import Flask, request
from pymongo import MongoClient, GEOSPHERE
import json
from bson.son import SON

app = Flask(__name__)
db_uri = 'mongodb://localhost:27017'
mongo_connect = MongoClient(db_uri)
db = mongo_connect['taxi_customer_db']
taxis = db['taxis']
customers = db['customers']

@app.route('/<string:user>/search', methods=['GET', 'POST'])
def search(user):
    user = user
    message = {}
    if request.method == 'POST':
        source_location = json.loads(request.form['source'])
        destination_location = request.form['destination']
        print(type(source_location), destination_location)
        range_query = {'location': SON([("$near", source_location), ("$maxDistance", 1000)])}
        for taxi in taxis.find().limit(2):
            message[taxi['id']] = {
                'name' : taxi['name'],
                'location' : taxi['location']
            }
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)