import RPi.GPIO as GPIO
import sys

from time import sleep
from picamera import PiCamera

dc=int(sys.argv[1]);

GPIO.setwarnings(False);

camera = PiCamera();

GPIO.setmode(GPIO.BCM);
GPIO.setup(3, GPIO.OUT);

led = GPIO.PWM(3, 200);
led.start(0);

led.ChangeDutyCycle(dc);

camera.start_preview()
camera.start_recording('/home/pi/record.h264')
sleep(float(sys.argv[2]))
camera.stop_recording()
camera.stop_preview()

led.ChangeDutyCycle(0);

