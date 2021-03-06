import dash
from dash import dcc as dcc
from dash import html as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from apps import overview, athlete


external_stylesheets = ["assets/1bootstrap.css", "assets/2style.css"]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets,
                #suppress_callback_exceptions = True,
                meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1"}])


server = app.server

nav = html.Div([
    dbc.Row([
        dbc.Col(html.Div(), className = "col-3"),
        dbc.Col(html.H1("Test Dashboard"), className = "col-6"),
        dbc.Col(html.Div(), className = "col-3")
    ]),
    dbc.Row([
        dbc.Col(html.Div(), className = "col-3"),
        dbc.Col(html.P(html.A("Overview", href="/overview")), className = "col-3"),
        dbc.Col(html.P(html.A("Athlete Improvement", href="/athlete")), className = "col-3"),
        dbc.Col(html.Div(), className = "col-3")
    ])
])



app.layout = html.Div([
    dcc.Location(id = "url", refresh = False),
    nav,
    html.Div(id = "page-content")
])


@app.callback(Output("page-content", "children"),
                Input("url", "pathname"))
def create_page_content(pathname):
    if pathname == "/overview":
        return overview.layout
    elif pathname == "/athlete":
        return athlete.layout
    else:
        return overview.layout

if __name__ == "__main__":
    app.run_server(host = "0.0.0.0",
                    port = 5000,
                    debug = True)



