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

    input_data = np.array([float(edu)/100, float(pet)/100, float(enter)/100, float(food)/100, float(med)/100, float(shop)/100, float(tran)/100]) 

    top_5_area = RecommenderEngine()

    return top_5_area.get_recommendations(input_data)

@auth.route('/dash', methods=['GET'])
def dash():

    postcode = request.args.get("postcode")

    return redirect('/dash/?postcode='+postcode)