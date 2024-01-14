import datetime
import speech_recognition as sr
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import string
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>12 and hour<18:
        speak("Good AfterNoon")

    else:
        speak("Good Evening")

    speak("I am Neo. How may I help")
    print("I am Neo. How may I help ?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please......")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendemail('youremail@gmail.com', to, content)
    server.close()

def passwordGen():
    length = int(input("Enter the length of the password as a count of its characters"))
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "{}[](),::./|\\?+=#$%^&@!*_-"

    upper, lower, nums, syms = True, True, True, True

    all = ""
    
    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols
    
    password = "".join(random.sample(all, length))
    print(password)





if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                print("Sorry , an error occured :(")
            
        elif 'password generator' in query:
            passwordGen()



        
