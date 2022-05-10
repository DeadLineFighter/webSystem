from flask import Flask
import dash
from dash import dcc, html       
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import urllib.parse
from sqlalchemy import false
from plotlyFunction import *

 #you need change path location
server = Flask(__name__)
#color
app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/',
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)

app.layout = html.Div([
        dcc.Location(id='url', refresh=False)
],id='page')

def bodylayout(p):

    return html.Div(children=[
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
    ], className='row'),
        html.Div([
            dcc.Graph(
                id='graph3',
                figure=property_pie_bar(p)
            ),  
        ], className='six columns')
    
])

@server.route('/')
def main():
    return 'hello world'

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
    server.run(host="127.0.0.1", port=5000,debug=false)