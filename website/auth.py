from flask import Blueprint, request, render_template, redirect, url_for
from model.recommender_engine import RecommenderEngine
from model.db import *
from bson import json_util
import numpy as np
# from collections import Counter

auth = Blueprint('auth', __name__)

@auth.route('/search', methods=['GET'])
def search():

    edu=request.values.get("edu")
    food=request.values.get("food")
    med=request.values.get("med")
    tran=request.values.get("tran")
    shop=request.values.get("shop")
    enter=request.values.get("enter")
    pet=request.values.get("pet")

    first_City = request.values.get("first_City")
    second_City = request.values.get("second_City")
    third_City = request.values.get("third_City")
    channels = request.values.get("channels")
    buget = request.values.get("buget")
    type = request.values.get("type")

    col = propertyCol.aggregate([
            {"$project":
                    {
                    "_id": 0,
                    "Name": 1,
                    "price": 1,
                    "channel": 1,
                    "county": 1,
                    "bathrooms": 1,
                    "bedrooms": 1,
                    "Description": 1,
                    "address": 1,
                    "Developer": 1,
                    "latitude": 1,
                    "longitude": 1,
                    "combine_property_type": 1,
                    "image": 1,
                    "listing ID":1
                    }},
            {"$match":
                    {
                    "$and":[{
                    "$or":[ {"county":first_City},
                            {"county":second_City},
                            {"county":third_City}]},
                            {"channel":channels},
                            {"price":{"$lte":int(buget)}},
                            {"combine_property_type":type}
            ]}}
    ])

    input_data = np.array([float(edu)/100, float(pet)/100, float(enter)/100, float(food)/100, float(med)/100, float(shop)/100, float(tran)/100]) 

    top_5_area = RecommenderEngine()

    list_col = list(col)

    y = top_5_area.get_recommendations(input_data)

    return render_template('map.html', list_col=list_col, y=y)

@auth.route('/map', methods=['GET'])
def test_dash():

    postcode = request.values.get("postcode")

    return redirect('/dash/?postcode='+postcode)

    # return render_template('map.html', x=x, y=y)
    #return top_5_area.get_recommendations(input_data) + json_util.dumps(col)