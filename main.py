import pyttsx3
import os
import subprocess as sp

import time
from datetime import datetime

import webbrowser as wb
import speech_recognition as sr

import random 

r = sr.Recognizer()


now = datetime.now()
current_time = now.strftime("%H")
current_time = int(current_time)
if (current_time >= 0) and (current_time < 12) :
    greeting = "Morning"
elif (current_time >= 12) and (current_time < 17) :
    greeting = "Afternoon"
else :
    greeting = "Evening"
print("Good " + greeting + " Sir")
pyttsx3.speak("Good " + greeting + " Sir")


print("I am San-era \nHow may I help you : ")
pyttsx3.speak("I am San-era \nHow may I help you : ")


while True:
    print("Waiting for your Command Sir :")
    source = None
    pyttsx3.speak("Waiting for your Command Sir :")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=8)
    got = random.choice(["Got it ,Sir", "Done sir","yes Sir","Ok sir"])
    pyttsx3.speak(got)
    try:
        req = r.recognize_google(audio)
    except:
        print("Sorry !! Due to some technical issue trying again ..")
        pyttsx3.speak("Sorry !!Due to some technical issue trying again .")
        continue
    req = req.lower()
    if ("don't " not in req) or ("dont " not in req) or ("not " not in req) :
        if ((("launch " in req) or ("start" in req) or ("want " in req) or ("surf " in req) or ("open " in req) or ("access " in req) or ("browse " in req)) and (("web" in req) or ("chrome" in req) or (" browser" in req) or ("internet" in req))) or (("web" in req) or ("chrome" in req) or ("browser" in req) or ("internet" in req)) :
            print("\nOpening Chrome Browser")
            pyttsx3.speak("Opening Chrome Browser")
            sp.getoutput('start chrome "http://google.com"')
        elif ((("launch " in req) or ("start" in req) or ("open" in req)) and (("notepad" in req) or ("editor" in req))) or (("write " in req) and (("want " in req) or ("text" in req))) or (("notepad" in req) or ("editor" in req)) :
            print("\nOpening Notepad")
            pyttsx3.speak("Opening Notepad")
            sp.getoutput('notepad')
        elif ((("launch " in req) or ("start" in req) or ("open" in req)) and (("calculator" in req) or ("cal" in req))) or (("do" in req) and (("maths " in req) or ("calculations" in req))) or (("arithmetic" in req)) :
            print("\nOpening Calculator")
            pyttsx3.speak("Opening Calculator")
            sp.getoutput("calc")
            time.sleep(3)

        elif ((("open " in req) or ("want " in req) or ("run" in req) or ("launch " in req) or ("listen ")) and (("linux" in req) or ("commnand" in req) or ("runner" in req))):
            print("\nOpening linux command runner")
            pyttsx3.speak("\nOpening linux command runner")
            sp.getoutput('start chrome "http://192.168.43.115/linuxcmd.html"')
            time.sleep(50)
        elif ("exit" in req) or ("close" in req) or ("farewell" in req) or ("bye" in req) or ((("i am" in req) or ("i'm" in req)) and (("done" in req) or ("good"))):
            now = datetime.now()
            current_time = now.strftime("%H")
            current_time = int(current_time)
            if (current_time >= 0) and (current_time < 12) :
                greeting = "\nHave a Good Day Sir"
            elif (current_time >= 12) and (current_time < 18) :
                greeting = "\nGood Evening Sir"
            else :
                greeting = "\nGood Night Sir"
                print(greeting)
                pyttsx3.speak(greeting)

            print("\nHope I was Helpful To You\nBye Bye 👋")
            pyttsx3.speak("\nHope I was Helpful To You\nBye Bye ")
            time.sleep(1)
            break
        else :
            print("Sorry, I was unable to process this commnand.")
            pyttsx3.speak("Sorry, I was unable to process this commnand.")

