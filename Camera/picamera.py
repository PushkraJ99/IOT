import picamera
from time import sleep

#Create Object for Picamera
camera = picamera.Picamera()

#Set Resolution
camera.resolution = (1024 , 768)
camera.brightness = 60
camera.start_preview()

#Add Text on Image
camera.annonate_text = "Hi Pi User"
sleep(5)

#Store Image
camera.capture('image.jpg')
camera.stop_preview()