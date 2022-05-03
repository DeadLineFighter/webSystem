from model import db
import dash
from dash import html,dcc,Input,Output,State,dash_table
import pandas as pd
import plotly.express as px
import pymongo
from bson.objectid import ObjectId

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='map')
])

@app.callback(
    Output('map','figure')
)