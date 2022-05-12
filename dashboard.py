import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from layouts import * 
import callbacks
import urllib.parse
from flask import Flask
from dash_ser import app,server


app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    nav_bar(),
    html.Div(id='page-content',style=CONTENT_STYLE) 
])

@app.callback(Output('page-content', 'children'), 
              [Input('url', 'pathname')]) 
def display_page(pathname):
    if pathname == '/dash/':
        return layout1
    elif pathname == '/dash/crime':
        return layout1
    elif pathname == '/dash/poi':
         return layout2
    elif pathname == '/dash/school':
        return layout3
    elif pathname == '/dash/property':
         return layout4
    else:
        return '404'


     
if __name__ == '__main__':
    app.run_server(port=5000, host= '127.0.0.1',debug=False)