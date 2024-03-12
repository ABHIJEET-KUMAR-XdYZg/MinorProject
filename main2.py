import bisect
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
#import selecting
# obtain audio from the microphone

def binary_search(lst, x):
    i = bisect.bisect_left(lst, x)
    if i != len(lst) and lst[i] == x:
        return True
    else:
        return False

def func():
    r = sr.Recognizer()
    isl_gif=['address', 'agra', 'ahemdabad', 'all', 'any questions', 'april', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore', 'be careful', 'bihar', 'bihar', 'bridge', 'can we meet tomorrow', 'cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile', 'dasara', 'deaf', 'december', 'deer', 'delhi', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money', 'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dollar', 'dont worry', 'duck', 'febuary', 'flower is beautiful', 'friday', 'fruits', 'glass', 'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'grapes', 'gujrat', 'had your lunch', 'happy journey', 'hello', 'hello what is your name', 'hindu', 'how many people are there in your family', 'hyderabad', 'i am a clerk', 'i am bore doing nothing', 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'i love to shop', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'lets go for lunch', 'litre', 'mango', 'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'my mother is a homemaker', 'my name is john', 'nagpur', 'nice to meet you', 'no smoking please', 'october', 'open the door', 'orange', 'pakistan', 'pass', 'please call me later', 'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'police station', 'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shall I help you', 'shall we go together tommorow', 'shop', 'sign language interpreter', 'sit down', 'sleep', 'southafrica', 'stand up', 'story', 'sunday', 'tamil nadu', 'take care', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village', 'voice', 'wait I am thinking', 'wednesday', 'weight', 'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job', 'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay', 'where is the bathroom', 'where is the police station', 'you are wrong']
    
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
    with sr.Microphone() as source:
            # image   = "signlang.png"
            # msg="HEARING IMPAIRMENT ASSISTANT"
            # choices = ["Live Voice","All Done!"] 
            # reply   = buttonbox(msg,image=image,choices=choices)
            r.adjust_for_ambient_noise(source)
            i=0
            while True:
                    print("I am Listening")
                    audio = r.listen(source)
                    # recognize speech using Sphinx
                    try:
                            a=r.recognize_google(audio)
                            a = a.lower()
                            print('You Said: ' + a.lower())
                            
                            for c in string.punctuation:
                                a= a.replace(c,"")
                                
                            if(a.lower()=='goodbye' or a.lower()=='good bye' or a.lower()=='bye'):
                                    print("oops!Time To say good bye")
                                    break
                            
                            elif(binary_search(isl_gif, a.lower())):
                                
                                class ImageLabel(tk.Label):
                                        """a label that displays images, and plays them if they are gifs"""
                                        def load(self, im):
                                            if isinstance(im, str):
                                                im = Image.open(im)
                                            self.loc = 0
                                            self.frames = []

                                            try:
                                                for i in count(1):
                                                    self.frames.append(ImageTk.PhotoImage(im.copy()))
                                                    im.seek(i)
                                            except EOFError:
                                                pass

                                            try:
                                                self.delay = im.info['duration']
                                            except:
                                                self.delay = 100

                                            if len(self.frames) == 1:
                                                self.config(image=self.frames[0])
                                            else:
                                                self.next_frame()

                                        def unload(self):
                                            self.config(image=None)
                                            self.frames = None

                                        def next_frame(self):
                                            if self.frames:
                                                self.loc += 1
                                                self.loc %= len(self.frames)
                                                self.config(image=self.frames[self.loc])
                                                self.after(self.delay, self.next_frame)
                                root = tk.Tk()
                                lbl = ImageLabel(root)
                                lbl.pack()
                                lbl.load(r'ISL_Gifs/{0}.gif'.format(a.lower()))
                                root.mainloop()
                            else:
                                for i in range(len(a)):
                                                if(a[i] in arr):
                                        
                                                        ImageAddress = 'letters/'+a[i]+'.jpg'
                                                        ImageItself = Image.open(ImageAddress)
                                                        ImageNumpyFormat = np.asarray(ImageItself)
                                                        plt.imshow(ImageNumpyFormat)
                                                        plt.draw()
                                                        plt.pause(0.8)
                                                else:
                                                        continue

                    except:
                            print(" ")
                    plt.close()

while 1:
  image   = "signlang.png"
  msg="HEARING IMPAIRMENT ASSISTANT"
  choices = ["Live Voice","All Done!"] 
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()