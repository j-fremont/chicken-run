import RPi.GPIO as GPIO
import sys

from flask import Flask, request, json, send_file
from flask_jsonpify import jsonify
from datetime import datetime
from time import sleep
from picamera import PiCamera
from os import listdir, remove

app = Flask(__name__)

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(3, GPIO.OUT);

led = GPIO.PWM(3, 200);

camera = PiCamera();

@app.route("/picture/new", methods = ['POST'])
def picture_new():
    now = datetime.now()
    dt_string = now.strftime("/%Y%m%d_%Hh%Mm%Ss")
    light_and_picture(dt_string)
    return jsonify({'result':'success'})

@app.route("/picture/get/<file>", methods = ['GET'])
def picture_get():
    return send_file('/home/pi/pictures/' + file, mimetype='image/jpeg')

@app.route("/picture/list", methods = ['POST'])
def picture_list():
    files = listdir('/home/pi/pictures')
    return jsonify({'files':files})

@app.route("/picture/remove/<file>", methods = ['POST'])
def picture_remove():
    remove('/home/pi/pictures/' + file)
    return jsonify({'result':'success'})

def light_and_picture(date_time):
    led.start(0);
    led.ChangeDutyCycle(100);
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/pictures/image_' + date_time + '.jpg')
    camera.stop_preview()
    sleep(2)
    led.ChangeDutyCycle(0);

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

