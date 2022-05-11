from flask import Flask
import dash
from dash import dcc, html       
from dash.dependencies import Input, Output
import urllib.parse
from model.plotlyFunction import *
from website.views import views
from website.auth import auth
import os

template_dir = os.path.dirname(os.path.abspath(__file__))+"\\template"

server = Flask(__name__, template_folder=template_dir)

external_scripts = ['https://d3js.org/d3.v5.min.js','https://cdnjs.cloudflare.com/ajax/libs/d3-cloud/1.2.5/d3.layout.cloud.min.js','https://cdnjs.cloudflare.com/ajax/libs/d3-tip/0.9.1/d3-tip.js']
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server.config['SECRET_KEY'] = 'DSA recommendation system FYP'

server.register_blueprint(views, url_prefix='/')
server.register_blueprint(auth, url_prefix='/')

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/',
    external_scripts=external_scripts,
    external_stylesheets=external_stylesheets
)

app.layout = html.Div([
        dcc.Location(id='url', refresh=False)
],id='page')

def bodylayout(p):

    x = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.Div([
            dcc.Graph(
                id='graph1',
                figure=crime_month_line(p)
            ),  
        ], className='six columns'),
        html.Div([
            dcc.Graph(
                id='graph2',
                figure=POI_type(p)
            ),  
        ], className='six columns'),
    ], className='row')
])

    return x

@app.callback(Output('page', 'children'),
              [Input('url', 'href')])
def display_page(href):
    print(href)
    if(href):
        param = urllib.parse.urlparse(href)
        param_dict = urllib.parse.parse_qs(param.query)
        if 'postcode' in param_dict.keys():
            return bodylayout(param_dict['postcode'][0])
    
    return html.H1('404 not found')

if __name__ == '__main__':
    server.run()  