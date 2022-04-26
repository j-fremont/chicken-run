import sys

from flask import Flask, request, json, send_file
from flask_jsonpify import jsonify
from datetime import datetime
from os import listdir, remove

app = Flask(__name__)

@app.route("/picture/get/<file>", methods = ['GET'])
def picture_get(file):
    print(file)
    return send_file('/home/j75550/' + file, mimetype='image/jpeg')

@app.route("/picture/list", methods = ['POST'])
def picture_list():
    files = listdir('/home/pi/pictures')
    return jsonify({'files':files})

@app.route("/picture/remove/<file>", methods = ['POST'])
def picture_remove(file):
    remove('/home/pi/pictures/' + file)
    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
