import sys
from flask import request,Response
from flask_restful import Resource
import numpy as np
import json
import pandas as pd
from itertools import combinations
from collections import Counter
from datetime import datetime
import random
from pathlib import Path


df = pd.read_csv(str(Path.cwd())+"/jetson-sample-data.csv")
df["item_per_quantity"] = df["price"]/df["quantity"]
pricelist = dict(zip(df["item_name"],df["item_per_quantity"]))
counts = df['item_name'].value_counts()


orders = df
item_pairs = list(combinations(set(orders['item_name']),2 ))
freq_counts = Counter()
for order_id, group in orders.groupby('order_id'):
    items = set(group['item_name'])
    for pair in combinations(items, 2):
        freq_counts[pair] += 1

# Create frequency dataframe
freq_df = pd.DataFrame.from_dict(freq_counts, orient='index', columns=['frequency'])
freq_df.index = pd.MultiIndex.from_tuples(freq_df.index, names=['item1', 'item2'])
freq_df = freq_df.reset_index()
freq_df = freq_df.sort_values('frequency', ascending=False)



class Recommendations(Resource):
    def get(self,num):
        print(int(num))
        print(freq_df.head(int(num)))
        data = freq_df.head(int(num));
        context = data.to_json();
        context = json.loads(context)
        return {'context':context},200


class ItemRecommendation(Resource):
    def post(self):
        body = request.get_json()
        item = body["item"]
        recommendations = freq_df[(freq_df['item1'] == item) | (freq_df['item2'] == item)]
        recommendations = recommendations[['item1', 'item2', 'frequency']]
        recommendations["probability"] = recommendations["frequency"]/counts[item]
        comboBreakEven = []
        for i in range(len(recommendations)):
            sumVal = pricelist[recommendations.iloc[i]["item1"]]+pricelist[recommendations.iloc[i]["item2"]]
            breakEven = sumVal - sumVal*0.6/100
            comboBreakEven.append(breakEven)
        recommendations["Combo_break_even_price"]=comboBreakEven
        recommendations = recommendations.head(100)
        context = recommendations.to_json();
        context = json.loads(context)
        return {"rows":len(recommendations),'context':context},200

class ClientRecommendation(Resource):
    def post(self):
        body = request.get_json()
        client = body["client"]
        clientRec = df[df["client_id"]==client]
        clientList = clientRec["item_name"]
        recommendations = freq_df[(freq_df['item1'].isin(clientList)) & (freq_df['item2'].isin(clientList))]
        recommendations = recommendations[['item1', 'item2', 'frequency']]
        recommendations["probability"] = recommendations["frequency"]/sum(recommendations["frequency"])
        recommendations = recommendations.head(100)
        context = recommendations.to_json();
        context = json.loads(context)
        return {"rows":len(recommendations),'context':context},200