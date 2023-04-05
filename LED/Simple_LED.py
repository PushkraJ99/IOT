import RPi.GPIO as GPIO
import time
from time import sleep

'''GPIO.setwarnings(False)'''

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
'''GPIO.setup(5,GPIO.OUT)'''
'''GPIO.setup(7,GPIO.OUT)'''



def  start():
	num= int(input('enter led number:'))
	GPIO.output(num,GPIO.HIGH)
	sleep(4)
	GPIO.output(num,GPIO.LOW)
	start()
	
start()
