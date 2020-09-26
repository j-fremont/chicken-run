#! /bin/bash

while true; do
	fswebcam -r 640x480 --no-banner /tmp/image.jpg
	sleep 60
done
