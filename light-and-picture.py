# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import sys

from time import sleep
from picamera import PiCamera
from datetime import datetime

dc=int(sys.argv[1]);

GPIO.setwarnings(False);

camera = PiCamera();

GPIO.setmode(GPIO.BCM);
GPIO.setup(3, GPIO.OUT);

led = GPIO.PWM(3, 200);
led.start(0);

led.ChangeDutyCycle(dc);

camera.start_preview()
sleep(5)
name = datetime.now().strftime("%Y-%m-%d_%H-%M_") + 'image.jpg'
camera.capture('/home/pi/chicken-run/chicken-server/images/' + name)
camera.stop_preview()
sleep(2)

led.ChangeDutyCycle(0);
