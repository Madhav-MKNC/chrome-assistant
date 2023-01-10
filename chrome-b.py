#!/bin/python3

# title: chrome-b
# author: Madhav Kumar [linkedin: ...............]
# created on: 4th December 2022 06:00 AM


#required modules
import pyttsx3 
import speech_recognition as sr 
import pyautogui as pg

# voice assistant
moon = pyttsx3.init('sapi5')
voices = moon.getProperty('voices')
moon.setProperty('voice', voices[1].id)

# UTILS

def speak(audio):
    print("Chrome-B is online")
    moon.say(audio)
    moon.runAndWait()

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"executing... [You said: {query}]")
    except Exception:
        print("command failed...") 
        query = ""
    # print(query)
    return query


def scroll(direction,x):
    pg.press(direction for i in range(x))

def shortcut(type,key):
    pg.keyDown(type)
    pg.press(key)
    pg.keyUp(type)

def nextTab(x):
    for i in range(x): shortcut('ctrl','tab')

def search(x):
    shortcut('ctrl','t')
    pg.write(x)
    pg.press('enter')

def close_tab():
    shortcut('ctrl','w')

def usekeyboard(x):
    pg.write(x)


# __main__

if __name__=="__main__" :
    speak("Chrome B is online")
    Command()
    speak("Program online now")

    while True:
        query = Command().lower()

        if 'scroll' in query:
            if 'up' in query: scroll('up',query.count('up'))
            else: scroll('down',query.count('down'))
        
        elif 'search' in query:
            query = " ".join(query.split()[query.split().index('search')+1:])
            # query = " ".join(query.split()[query.split().index('search')+1:]).lower().replace('for me','')
            search(query)            

        elif 'cancel' in query or 'close' in query: close_tab()

        elif 'tab' in query or 'tap' in query or 'ap' in query: nextTab(query.count('a'))

        elif 'write' in query:
            query = " ".join(query.split()[query.split().index('write')+1:]).replace('uppercase','').replace('lowercase','')
            if 'uppercase' in query: usekeyboard(query.upper())
            elif 'lowercase' in query: usekeyboard(query.lower())
            else: speak("sorry what?")

        elif 'sleep' in query: 
            speak("I'm out, bye.")
            exit()

