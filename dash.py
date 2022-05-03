from model import db
import dash
from dash import html,dcc,Input,Output,State,dash_table
import pandas as pd
import plotly.express as px
import pymongo
from bson.objectid import ObjectId
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

myclient = pymongo.MongoClient("mongodb://ia.dsa.21.a:tuJ6ZdJGWrEf8SAd6gb8ZaHUcs83HHJu@18.189.210.178:27017/?authSource=IA&readPreference=primary&directConnection=true&ssl=false")
mydb = myclient["Ukdata"]
mycol = mydb["Crime"]

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'UK Dashboard'


#########header#########
colors = {
    'background': '#111111',
    'bodyColor':'#F2DFCE',
    'text': '#7FDBFF'
}
def get_page_heading_style():
    return {'backgroundColor': colors['background']}

def get_page_heading_title():
    return html.H1(children='UK Crime Dashboard',
                                        style={
                                        'textAlign': 'center',
                                        'color': colors['text']
                                    })

def get_page_heading_subtitle():
    return html.Div(children='Count crime cases from each region',
                                         style={
                                             'textAlign':'center',
                                             'color':colors['text']
                                         })

def generate_page_header():
    main_header =  dbc.Row(
                            [
                                dbc.Col(get_page_heading_title(),md=12)
                            ],
                            align="center",
                            style=get_page_heading_style()
                        )
    subtitle_header = dbc.Row(
                            [
                                dbc.Col(get_page_heading_subtitle(),md=12)
                            ],
                            align="center",
                            style=get_page_heading_style()
                        )
    header = (main_header,subtitle_header)
    return header
        
########View#######
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


########Controller#######
@app.callback(
    Output('map-with-slider','figure'),
    [Input('year-slider','value')])
def map_from_uk(year):