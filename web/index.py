import dash
from dash import dcc as dcc
from dash import html as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


external_stylesheets = ["assets/1bootstrap.css", "assets/2style.css"]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets,
                suppress_callback_exceptions = True,
                meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1"}])


server = app.server






