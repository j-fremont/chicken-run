import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import requests
import json

from dash.dependencies import Input, Output

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
                        dbc.Button("Afficher la photo", color="primary", className="mr-1"),
                        dbc.Button("Supprimer la photo", color="primary", className="mr-1")
                    ])
                ]),
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

@app.callback(
    Output("file_list", "options"),
    [Input("dummy", "children"),]
)
def on_init(n):
    response = requests.post('http://192.168.1.62:5000/picture/list')
    files = json.loads(response.text)['files']
    return [{'label': file, 'value': file} for file in files]

@app.callback(
    Output("file_list", "options"), [Input("take_picture", "n_clicks"),]
#    Output("card_image", "src"), [Input("take_picture", "n_clicks"),]
)
def on_take_picture(n):
    return app.get_asset_url('image.jpg')

#@app.callback(
#    [Input(component_id='file_list', component_property='value'),]
#)
#def update_file(file):
#    print file

if __name__ == '__main__':
    app.run_server(debug=True)
    
