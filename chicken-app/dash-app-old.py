# -*- coding: utf-8 -*-

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import requests
import json
#import asyncio

from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Form([
                dbc.FormGroup([
                    dbc.Button("Prendre une nouvelle photo", id="take_picture", color="primary", className="mr-1"),
                ]),
                dbc.FormGroup([
                    dbc.Label("Liste des photos", html_for="dropdown"),
                    dcc.Dropdown(
                        id="file_list",
                        options=[
                            {"label": "Option 1", "value": 1},
                            {"label": "Option 2", "value": 2},
                        ],
                    ),
                    html.Div(id='dummy')
                ]),
                dbc.FormGroup([
                    dbc.ButtonGroup([
                        dbc.Button("Afficher la photo", id="get_picture", color="primary", className="mr-1"),
                        dbc.Button("Supprimer la photo", id="delete_picture", color="primary", className="mr-1")
                    ])
                ]),
                dbc.Alert("", id="alert", dismissable=True, is_open=False),
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardImg(id="card_image", top=True),
                dbc.CardBody(
                    html.P("This card has an image at the top", id="card_label", className="card-text")
                ),
            ], style={"width": "18rem"})
        ], width=9),
    ])
], style = {
    "position": "relative",
    "top": "25px",
    "left": "25px"
    }
)

#async def post_picture_list():
#    response = await requests.post('http://192.168.1.62:5000/picture/list')
#    files = json.loads(response.text)['files']
#    return [{'label': file, 'value': file} for file in files]

@app.callback(
    Output("file_list", "options"),
    Input("dummy", "children")
)
def on_init(n):
    response = requests.post('http://192.168.1.62:5000/picture/list')
    files = json.loads(response.text)['files']
    files.sort()
    #print(files)
    return [{'label': file, 'value': file} for file in files], False
    #return asyncio.run(poste_picture_list())

@app.callback(
    Output("card_image", "src"), [Input("take_picture", "n_clicks"),]
)
def on_take_picture(n):
    #requests.get('http://192.168.1.62:5000/picture/new')
    return app.get_asset_url('image.jpg')

@app.callback(
    Output("alert", "is_open"),
    Output("alert", "color"),
    Output("alert", "children"),
    Input("take_picture", "n_clicks"),
    Input("get_picture", "n_clicks"),
    Input("delete_picture", "n_clicks"),
    State('file_list', 'value')
)
def on_get_picture(take, get, delete, file):

    ctx = dash.callback_context

    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split('.')[0]

        if input_id == 'take_picture':
            return True, 'primary', 'Ok'

        if input_id == 'get_picture':
            r = requests.get('http://192.168.1.62:5000/picture/get/' + file, allow_redirects=True)
            open('assets/' + file, 'wb').write(r.content)
            return True, 'primary', 'Ok'

        if input_id == 'delete_picture':
            requests.post('http://192.168.1.62:5000/picture/remove/' + file)
            return True, 'primary', 'Ok'

#        if input_id == 'dummy':
#            return False, 'primary', ''

    return True, 'primary', 'Ok'

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port='8051', debug=True)
