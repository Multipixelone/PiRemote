## Just FYI, this probably COULD be coded cleaner... If you think you could help, feel free to submit a pull request!
## Import Files
print('eyeRemote by Multipixelone on Github.')
from TakePicture import TakePicture
import picamera
from LocalVariables import takepicture
print('Imported Picture Taking')
import Cloudsight
from Cloudsight import UploadPicture
import cloudsight
print('Imported Image Uploading')
import RPi.GPIO as GPIO
print('Imported GPIO')
from PlaySounds import Welcome
from PlaySounds import ErrorNetwork
from PlaySounds import SpeakWord
print('Imported Sound Playing')
from time import sleep
print('Imported Sleeping')

## Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(takepicture,GPIO.IN)

## Functions Available:
#TakePicture()
#UploadPicture()
#ErrorNetwork()
#Welcome()
#SpeakWord(WORD)

## Code to upload image.jpg, return a json response, import that, and then speak it out
#UploadPicture()
#from CloudsightAPI import item
#SpeakWord(item)

## Code to take picture:
#print('Waiting for inputs!')
#while True:
#  if (GPIO.input(takepicture)):
#    TakePicture()



## Actual code now: 
Welcome()
print('Waiting for inputs!')
while True:
  if (GPIO.input(takepicture)):
    SpeakWord("Taking Picture")
    TakePicture()
    try:
        UploadPicture()
    except cloudsight.ConnectionError: ## Might need to be changed after the program shift
         ErrorNetwork()
    else:
         from CloudsightAPI import item
         SpeakWord(item)

    
