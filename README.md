# chicken-run

Permet d'éclairer et de filmer l'intérieur d'une cabana oiseau.

Lancer.

```
capture.sh
```

Installer Picamera2 (https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf) et ffmpeg pour les films.

```
sudo apt update
sudo apt install -y python3-picamera2
sudo apt install -y ffmpeg
```

Pour streamer avec VLC. Co�té Raspberry.

```
libcamera-vid -t0 --width 1920 --height 1080 --framerate 10 --nopreview --codec h264 --profile high --intra 5 --listen -o tcp://0.0.0.0:8494
```

Côté VLC.


```
vlc tcp/h264://192.168.1.46:8494
```

Ne plus utiliser la page Webcam dans le wiki, correspond a l'ancienne lib cam�ra.
