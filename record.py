import sys

from time import sleep
from picamera import PiCamera

camera = PiCamera();

camera.start_preview()
camera.start_recording('/home/pi/record.h264')
sleep(float(sys.argv[1]))
camera.stop_recording()
camera.stop_preview()

