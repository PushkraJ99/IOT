import RPi.GPIO as GPIO
from mfrc52 import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522()

try:
	text = input("Enter data to Write on the tag : ")
	print("Now place your tag to Write")#
	reader.write(text)
	print("Sucessfully Wrote data onto tag")
except Exception as e:
	print("Exception is ",e)
	
sleep(6)

print()
print("Place Your Card to Scan")

try:
	id ,text = reader.read()
	print("The Data on the tag is ",text)
	print("Id of Your tag is ",id)
except Exception as e:
	print("Exception is ",e)
finally:
	GPIO.cleanup()
