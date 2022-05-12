import dash
import dash_bootstrap_components as dbc
from flask import Flask


server = Flask(__name__)
# external_scripts = ['https://d3js.org/d3.v5.min.js','https://cdnjs.cloudflare.com/ajax/libs/d3-cloud/1.2.5/d3.layout.cloud.min.js','https://cdnjs.cloudflare.com/ajax/libs/d3-tip/0.9.1/d3-tip.js']
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    __name__,
    server=server,
    # routes_pathname_prefix='/dash/',
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)
app.title = 'UK Dashboard'
