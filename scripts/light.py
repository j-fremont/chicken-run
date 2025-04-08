# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import sys

from time import sleep

dc=int(sys.argv[1]);

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(3, GPIO.OUT);

led = GPIO.PWM(3, 200);
led.start(0);
led.ChangeDutyCycle(dc);

sleep(float(sys.argv[2]));

led.ChangeDutyCycle(0);
