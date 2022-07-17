# Nibble

## Inspiration
I have a rabbit and wanted to make something hardware-related that would help rabbit owners like myself keep track of their weight as it plays a huge part in their health and overall quality of life. Unfortunetly, I have to leave my rabbit at home sometimes when I visit places for long periods of times, which leaves me to worry about my pet's health and weight developing while at home.

## What it does
Nibble is a system that basically is a weight scale system made with load sensors to give an exact weight in pounds of whatever you want to be weighed. For this project, we wanted to take the weight of my rabbit and will get emailed results and the next steps on how to manage its weight (given if the result is underweight or overweight). To tie into the theme of SelfieHacks II, we also have a section of our hardware prototype that takes a picture of the rabbit, while it's still (and getting its weight checked) and will send an email with picture and weight information along with tips based on the weight it recorded. You can train your pet to go into the device at specific times for them to send you information about your pet while you are not at home.

## How we built it
Created a weight scale using a kitchen plate and multiple load-strain sensors, we would get the weight with an Arduino UNO that would output it on an LCD. To ensure that a rabbit or other similar pets entered the device, a PIR motion sensor is also used to detect presence of an animal and along with a weight minimum, will trigger the device. We used a camera from a tablet to capture a picture of the animal we are weighing and send you an email using the Twilio SendGrid API. 

## Challenges we ran into
Linking the file of the photo for upload. We also wanted our photo to upload to a social media platform. We tried to upload to Twitter, Instagram, and Facebook but the processes were too long for the amount of time we had, and sometimes there were to many tests to configure. The Instagram API then locked us out for sending too many requests which prevented us from using it any further. We just stuck with email format instead and ditch what we originally planned :(

## Accomplishments that we're proud of
Getting an actual physical prototype made, making a scale that has very accurate results and building something useful with a social media twist (attempted lol) that other pet owners can use. The email system was also something that we were proud of as well.

## What's next for Nibble
We would want this product to work for all house animals like cats and dogs, not just rabbits. I only had a rabbit, so for our initial prototype, we just surrounded this submission around my rabbit. We also did not account for different breeds and different stages of life as those have different weight averages. We set the function in the code to match my rabbits breed and age, we hope to make a feature to account for more breeds and more ages. We also want to replace the tablet with an actual Raspberry Pi instead and also use a Contactless Thermometer Module to take temperature readings to go along with weight.
