
import sys
from flask import request,Response,jsonify,Flask
from flask_restful import Resource
import numpy as np
import json
from flask_pymongo import PyMongo
from bson import ObjectId

# Instantiation
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/recommendations'
mongo = PyMongo(app)



# Database
orders = mongo.db.orders
clients = mongo.db.clients




class Orders(Resource):
    def get(self):
        orders = []
        for doc in orders.find():
            orders.append({
                '_id': str(ObjectId(doc['_id'])),
                'client_id': doc['client_id'],
                'order_id': doc['order_id'],
                'item_name': doc['item_name'],
                'quantity': doc['quantity'],
                'price': doc['price'],
                "date":doc["date"]
            })

        print(10)
        return jsonify(orders)
    

class Client(Resource):
    def post(self):
        print(request.json)
        data = request.json
        id = clients.insert_one(data)
        return {"response":"Data Inserted successfully"},200
    
    
    def get(self):
        users = []
        for doc in clients.find():
            users.append({
                '_id': str(ObjectId(doc['_id'])),
                'name': doc['name'],
                'email': doc['email'],
                "clientId":doc["clientId"]
            })

        print(10)
        return jsonify(users)
