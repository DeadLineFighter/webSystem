from model import db
import dash
from dash import html,dcc,Input,Output,State,dash_table
import pandas as pd
import plotly.express as px
import pymongo
from bson.objectid import ObjectId
import plotly.graph_objs as go

myclient = pymongo.MongoClient("mongodb://ia.dsa.21.a:tuJ6ZdJGWrEf8SAd6gb8ZaHUcs83HHJu@18.189.210.178:27017/?authSource=IA&readPreference=primary&directConnection=true&ssl=false")
mydb = myclient["Ukdata"]
mycol = mydb["Crime"]

app = dash.Dash()

server = app.server

app.layout = html.Div([
    dcc.Graph(id='map-with-slider'),
    dcc.Slider(
        id='year-slider',
        min= 2017,
        max = 2020,
        value=2017,
        step=1,
        marks={year:str(year) for year in [2017,2018,2019,2020]}
    )
])

@app.callback(
    Output('map-with-slider','figure'),
    [Input('year-slider','value')]
)

