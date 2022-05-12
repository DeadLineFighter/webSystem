import dash
import dash_bootstrap_components as dbc
from flask import Flask


server = Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
    # routes_pathname_prefix='/dash/',
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)
app.title = 'UK Dashboard'
