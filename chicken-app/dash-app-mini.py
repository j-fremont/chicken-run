import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import requests
import json
import wget

from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(id="card_image", top=True),
                dbc.CardBody(
                    html.P("This card has an image at the top", id="card_label", className="card-text")
                ),
            ], style={"width": "18rem"}),
            html.Div(id='dummy')
        ], width=12),
    ])
], style = {
    "position": "relative",
    "top": "25px",
    "left": "25px"
    }
)

@app.callback(
    Output("card_image", "src"),
    [Input("dummy", "children")]
)
def on_init(n):
    #wget.download('http://127.0.0.1:5000/picture/get/1648020012141.jpeg', out='/home/j75550/test.jpeg')
    response = requests.get('http://localhost:5000/picture/get/1648020012141.jpeg', headers={'User-Agent': 'Mozilla/5.0'})
    print(response.url)
    print(response.status_code)
    #if response.status_code == 200:
    #    with open('/tmp/test.jpeg', 'wb') as f:
    #        f.write(response.content)

    #response = requests.get(, allow_redirects=True)
    #open('test.jpeg', 'wb').write(response.content)
    #print(response.content)
    return True

if __name__ == '__main__':
    app.run_server(debug=True)
