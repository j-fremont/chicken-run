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
sleep(5)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()
sleep(2)

led.ChangeDutyCycle(0);

