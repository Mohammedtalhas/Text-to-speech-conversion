from gtts import gTTS
import os
import csv
path = 'D:/DATA/projc'
for filename in os.listdir(path):
    if filename == 'mp3.txt':
        x = open(filename)
        tts = gTTS(text=x.read(), lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
