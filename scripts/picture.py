# -*- coding: utf-8 -*-

from picamera import PiCamera
from datetime import datetime
from time import sleep

camera = PiCamera();

camera.start_preview()
sleep(5)
name = datetime.now().strftime("%Y-%m-%d_%H-%M_") + 'image.jpg'
camera.capture('../chicken-server/images/' + name)
camera.stop_preview()
camera.close()
sleep(2)
