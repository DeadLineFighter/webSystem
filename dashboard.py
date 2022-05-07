import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app, server 
from layouts import * 
import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    nav_bar(),
    html.Div(id='page-content',style=CONTENT_STYLE) 
])

@app.callback(Output('page-content', 'children'), 
              [Input('url', 'pathname')]) 
def display_page(pathname):
    if pathname == '/':
        return layout1
    elif pathname == '/crime':
        return layout1
    elif pathname == '/poi':
         return layout2
    else:
        return '404'

     
if __name__ == '__main__':
    app.run_server(port=8050, host= '0.0.0.0',debug=False)