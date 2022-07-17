
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from instapy_cli import client
import cv2
import serial
import time
import os
from twilio.rest import Client
import base64
import requests
import asyncio
import shutil
import imgbbpy

global Weight
global status
global caption
Weight = 0
status = ""
Fimage = ""
caption = ""

def pic(img):
    global Fimage
    client = imgbbpy.SyncClient('5f7062449d9d5de38c9baba23b812663')
    image = client.upload(file=img)
    Fimage = image.url
    print(Fimage)


def send_email(img,status):
   message = Mail(
    from_email='petwatch001@gmail.com',
    to_emails='ridwan3968@gmail.com',
    subject='Image and information of your rabbit',
    html_content=("Here is the image of your rabbit after detection, and weight information:  <br> <img src={0} alt='Felix'><br><strong>Your rabbit weight measured is {1}</strong><strong></strong><strong> pounds.</strong><br><strong>{2}</strong>".format(img,Weight,status)),
)
   sg = SendGridAPIClient('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')
   response = sg.send(message)
def sendInstagram(img,c):
    from instabot import Bot

    bot = Bot()
    bot.login( username = "PetWatchUnit4",  password = "somepassword")

    
    bot.upload_photo("\PET_0.png", caption=c)


arduino = serial.Serial('COM5',9600,timeout=0.1)
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0


while True:
    trigger = arduino.readline().strip().decode("utf-8")
    print(trigger)
    ret, frame = cam.read()
    if not ret:
        print("failed to get picture")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        break
    elif trigger != "":
        
        Weight = trigger
        
        img_name = "PET_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        file = os.path.splitext(img_name)
        only_name = file[0]
        extension = file[1]
        
        new_base = only_name + '_new' + extension
  
        new_name = os.path.join("Rabbit Images", new_base)
        
        
        
        pic(img_name)
        
        if bool(trigger) > 4.0:
            status = "Your rabbit is overweight"
        elif bool(trigger) < 1.0:
            status = "Your rabbit is underweight"
        send_email(Fimage,status)
        sendInstagram(Fimage,caption)
        caption = ("Weight: "+Weight+" lbs")
   
        print("{} ANIMAL DETECTED, IMAGE TAKEN".format(img_name))
        img_counter += 1
       




        
        time.sleep(20)
    
cam.release()

cv2.destroyAllWindows()
