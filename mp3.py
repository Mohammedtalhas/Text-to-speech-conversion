from gtts import gTTS
import os
import csv
path = ''# mention ur path of the text file
for filename in os.listdir(path):
    if filename == 'mp3.txt': #place the name of the file as I've just given an example 
        x = open(filename)
        tts = gTTS(text=x.read(), lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
