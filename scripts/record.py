# -*- coding: utf-8 -*-

import sys

from picamera2 import Picamera2
from datetime import datetime

camera = Picamera2();
name = datetime.now().strftime("%Y-%m-%d_%H-%M_") + 'movie.mp4'
camera.start_and_record_video('../chicken-server/movies/' + name, duration=int(sys.argv[1]))
