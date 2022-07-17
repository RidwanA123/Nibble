
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


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
    client = imgbbpy.SyncClient('API KEY')
    image = client.upload(file=img)
    Fimage = image.url
    print(Fimage)


def send_email(img,status):
  if status == "U":
    message = Mail(
    from_email='petwatch001@gmail.com',
    to_emails='ridwan3968@gmail.com',
    subject='Image and information of your rabbit',
    html_content=("Here is the image of your rabbit after detection, and weight information:  <br> <img src={0} alt='Felix'><br><strong>Your rabbit weight measured is {1}</strong><strong></strong><strong> pounds.</strong><br>Your rabbit is <strong>underweight: </strong><br>Rabbit’s need to eat food in order to gain healthy weight. Regardless of weight, a rabbits diet should comprise mostly of hay with some greens, vegetables and fruit.<br>Consider<br>Offer them new foods they aren’t used to, given that it is safe and nutritious for the rabbit<br>Change the brand of hay or pellets you feed them<br>Increase the amount of water they drink on a daily basis<br>If your rabbit refuses to eat, consider helping them by feeding them manually<br>Take a plastic syringe, i.e., one without a needle.<br>Best of luck to you and your rabbit :)<br>".format(img,Weight,status)),
)
    sg = SendGridAPIClient('API KEY')
    response = sg.send(message)
  elif status == "O":
    message = Mail(
    from_email='petwatch001@gmail.com',
    to_emails='ridwan3968@gmail.com',
    subject='Image and information of your rabbit',
    html_content=("Here is the image of your rabbit after detection, and weight information:  <br> <img src={0} alt='Felix'><br><strong>Your rabbit weight measured is {1}</strong><strong></strong><strong> pounds.</strong><br>Your rabbit is <strong>overweight: </strong><br>The main cause of obesity or any sort of significant above average weight gain is mainly overeating. To gain weight, rabbits take in more calories than they are exerting, leading to an accumulation of weight. Another factor is that rabbits being caged for a significant amount of time of their lifes, rabbits are vulnerable to weight gain when they dont get time exercising and overall a balance of diet and exercise.<br>Consider:<br>- Cutting back on sugary and fat filled foods and the amount of treats you give your rabbit.<br>- Not letting your rabbit be stationary, and let your rabbit out of the cage as they are inclined to roam and jump around in the wild. Let them outside like in your backyard or take them on walks with a proper leash.<br>- Along with their exercise, give them greens and fruits for meals.<br>Best of luck to you and your rabbit :)<br>".format(img,Weight,status)),
)
    sg = SendGridAPIClient('API KEY')
    response = sg.send(message)
  else:
    message = Mail(
    from_email='petwatch001@gmail.com',
    to_emails='ridwan3968@gmail.com',
    subject='Image and information of your rabbit',
    html_content=("Here is the image of your rabbit after detection, and weight information:  <br> <img src={0} alt='Felix'><br><strong>Your rabbit weight measured is {1}</strong><strong></strong><strong> pounds.</strong>".format(img,Weight,status)),
)
    sg = SendGridAPIClient('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')
    response = sg.send(message)




arduino = serial.Serial('COM5',9600,timeout=0.1)
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0


while True:
    trigger = arduino.readline().strip().decode("utf-8")
  
   
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
        if float(trigger) >= 4.0:
            status = "O"
            
        elif float(trigger) <= 1.0:
            status = "U"
           
        Weight = trigger
        
        img_name = "PET_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        file = os.path.splitext(img_name)
        only_name = file[0]
        extension = file[1]
        
        new_base = only_name + '_new' + extension
  
        new_name = os.path.join("Rabbit Images", new_base)
        
        
        
        pic(img_name)
        
        
        send_email(Fimage,status)
        
        caption = ("Weight: "+Weight+" lbs")
   
        print("{} ANIMAL DETECTED, IMAGE TAKEN".format(img_name))
        img_counter += 1
       




        
        time.sleep(20)
    
cam.release()

cv2.destroyAllWindows()
