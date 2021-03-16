import RPi.GPIO as GPIO
import sys

from time import sleep
from picamera import PiCamera

def light_and_picture(date_time):
    GPIO.setwarnings(False);

    camera = PiCamera();

    GPIO.setmode(GPIO.BCM);
    GPIO.setup(3, GPIO.OUT);

    led = GPIO.PWM(3, 200);
    led.start(0);
    
    led.ChangeDutyCycle(100);

    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/pictures/image_' + date_time + '.jpg')
    camera.stop_preview()
    sleep(2)

    led.ChangeDutyCycle(0);

