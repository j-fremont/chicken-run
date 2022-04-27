# -*- coding: utf-8 -*-

import sys

from flask import Flask, request, json, send_file
from flask_jsonpify import jsonify
from os import listdir, remove

app = Flask(__name__)

@app.route("/image/list", methods = ['GET'])
def picture_list():
	files = listdir('images')
	return jsonify({'files':files})

@app.route("/image/get/<file>", methods = ['GET'])
def picture_get(file):
	return send_file('images/' + file, mimetype='image/jpeg')

@app.route("/image/remove/<file>", methods = ['POST'])
def picture_remove(file):
	remove('images/' + file)
	return jsonify({'result':'success'})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
