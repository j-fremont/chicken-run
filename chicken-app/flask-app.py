import RPi.GPIO as GPIO
import sys
import mycamera

from flask import Flask, request, json, send_file
from flask_jsonpify import jsonify
from datetime import datetime
from os import listdir, remove

app = Flask(__name__)

@app.route("/picture/new", methods = ['GET'])
def picture_new():
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d_%Hh%Mm%Ss")
    mycamera.light_and_picture(dt_string)
    return send_file('/home/pi/pictures/image_' + dt_string + '.jpg', mimetype='image/jpeg')

@app.route("/picture/get/<file>", methods = ['GET'])
def picture_get():
    return send_file('/home/pi/pictures/' + file, mimetype='image/jpeg')

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

