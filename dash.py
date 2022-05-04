from model.db import db
import dash
import pandas as pd
import plotly.express as px
import pymongo
import os
# import dash_html_components as html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc


myclient = pymongo.MongoClient("mongodb://ia.dsa.21.a:tuJ6ZdJGWrEf8SAd6gb8ZaHUcs83HHJu@18.189.210.178:27017/?authSource=IA&readPreference=primary&directConnection=true&ssl=false")
mydb = myclient["Ukdata"]
mycol = mydb["Crime"]

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'UK Dashboard'


#########header#########
# colors = {
#     'background': '#111111',
#     'bodyColor':'#F2DFCE',
#     'text': '#7FDBFF'
# }
# def get_page_heading_style():
#     return {'backgroundColor': colors['background']}

# def get_page_heading_title():
#     return html.H1(children='UK Crime Dashboard',
#                                         style={
#                                         'textAlign': 'center',
#                                         'color': colors['text']
#                                     })

# def get_page_heading_subtitle():
#     return html.Div(children='Count crime cases from each region',
#                                          style={
#                                              'textAlign':'center',
#                                              'color':colors['text']
#                                          })

# def generate_page_header():
#     main_header =  dbc.Row(
#                             [
#                                 dbc.Col(get_page_heading_title(),md=12)
#                             ],
#                             align="center",
#                             style=get_page_heading_style()
#                         )
#     subtitle_header = dbc.Row(
#                             [
#                                 dbc.Col(get_page_heading_subtitle(),md=12)
#                             ],
#                             align="center",
#                             style=get_page_heading_style()
#                         )
#     header = (main_header,subtitle_header)
#     return header
        
########View#######
# app.layout = html.Div([
#     dcc.Graph(id='map-with-slider'),
#     dcc.Slider(
#         id='year-slider',
#         min= 2017,
#         max = 2020,
#         value=2017,
#         step=1,
#         marks={year:str(year) for year in [2017,2018,2019,2020]}
#     )
# ])
trace = go.Bar(x=db.monthCrime.crime, y=db.monthCrime.count, name='crime')

app.layout = html.Div(children=[html.H1("CData Extension + Dash", style={'textAlign': 'center'}),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace],
            'layout':
            go.Layout(title='UK crime Data', barmode='stack')
        })
], className="container")

########Controller#######
# @app.callback(
#     Output('map-with-slider','figure'),
#     [Input('year-slider','value')])
# def map_from_uk(year):

if __name__ == '__main__':
    app.run_server(debug=True)