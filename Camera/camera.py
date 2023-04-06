import picamera
from time import sleep

camera = picamera.PiCamera()

camera.resolution = (1024, 768)
camera.brightness = 60
camera.start_preview()

camera.annotate_text = 'Hi Pi User'
sleep(5)

camera.capture('image2.jpeg')
camera.stop_preview()