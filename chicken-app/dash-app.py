import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Form([
                dbc.FormGroup([
                    dbc.Button("Prendre une nouvelle photo", color="primary", className="mr-1"),
                ]),
                dbc.FormGroup([
                    dbc.Label("Liste des photos", html_for="dropdown"),
                    dcc.Dropdown(
                        id="dropdown",
                        options=[
                            {"label": "Option 1", "value": 1},
                            {"label": "Option 2", "value": 2},
                        ],
                    ),
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
dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            html.P("This card has an image at the top", className="card-text")
        ),
    ],
    style={"width": "18rem"},
)

        ], width=9),
    ])
], style = {
    "position": "relative",
    "top": "25px",
    "left": "25px"
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
    
