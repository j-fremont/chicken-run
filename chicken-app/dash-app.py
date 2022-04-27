# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import requests
import json

from dash.dependencies import Input, Output, State

proxies = {
	"http": None,
	"https": None
}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

app.title = 'Chicken run'
app._favicon = "favicon.ico"

app.layout = html.Div([
	dbc.Row([
		dbc.Col([
			dbc.Form([
				dbc.FormGroup([
					dbc.Label("Liste des photos", html_for="dropdown"),
					dcc.Dropdown(id="file_list", persistence=True),
					html.Div(id='dummy_list')
				]),
				dbc.Alert("", id="alert", dismissable=True, is_open=False),
			]),
		], width=3),
		dbc.Col([
			dbc.Card([
				dbc.CardImg(id="card_image", top=True),
				dbc.CardBody(id="card_body"

				),
				html.Div(id='dummy_image')
			], style={"width": "45rem"})
		], width=9),
	])
], style = {
	"position": "relative",
	"top": "25px",
	"left": "25px"
	}
)

@app.callback(
	Output("card_image", "src"),
	[Input("dummy_image", "children"),
	Input("file_list", "value")]
)
def on_init_image(dummy_image, file_list):
	if file_list == None:
		name = 'last.jpg'
	else:
		name = file_list
	response = requests.get('http://localhost:5000/image/get/' + name, proxies=proxies)
	if response.status_code == 200:
		with open('assets/image.jpg', 'wb') as f:
			f.write(response.content)
	return app.get_asset_url('image.jpg')

@app.callback(
	Output("file_list", "options"),
	[Input("dummy_list", "children")]
)
def on_init_list(dummy_list):
	list = []
	response = requests.get('http://localhost:5000/image/list', proxies=proxies)
	data = json.loads(response.content)
	for item in data['files']:
		if item != 'last.jpg':
			list.append({
				'label': item,
				'value': item
			})
	return sorted(list, key=lambda d: d['value'])

@app.callback(
	Output("card_body", "children"),
	[Input("file_list", "value")]
)
def on_init_image(file_list):
	return html.P(file_list, className="card-text")

if __name__ == '__main__':
	app.run_server(debug=True)
