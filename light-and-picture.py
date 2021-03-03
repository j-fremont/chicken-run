import RPi.GPIO as GPIO

from time import sleep
from picamera import PiCamera

camera = PiCamera();

GPIO.setmode(GPIO.BCM);
GPIO.setup(3, GPIO.OUT);

led = GPIO.PWM(3, 200);
led.start(0);

led.ChangeDutyCycle(100);

camera.start_preview()
sleep(5)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()
sleep(2)

led.ChangeDutyCycle(0);

