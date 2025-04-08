# -*- coding: utf-8 -*-

from picamera2 import Picamera2, Preview
from datetime import datetime
from time import sleep

camera = Picamera2();
camera_config =	camera.create_preview_configuration() 
camera.configure(camera_config)
camera.start_preview(Preview.DRM)
camera.start()
sleep(5)
name = datetime.now().strftime("%Y-%m-%d_%H-%M_") + 'image.jpg'
camera.capture_file('../chicken-server/images/' + name)
camera.stop_preview()
camera.close()
sleep(2)
