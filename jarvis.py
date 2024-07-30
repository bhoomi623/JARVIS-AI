import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import cv2
import random
from  requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
# to convert voice to text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said{query}")


    except Exception as e:
        speak("say that again please...")
        return 'none'
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("i am jarvis mam please tell me how can i help you")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('email id', 'pass')
    server.sendemail('your email id',to,content)
    server.close()








if __name__ == "__main__":
    wish()
    while True:
    #if 1:

        query= takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:

            os.system("start cmd")

        elif "open spotify" in query:
            apath = "C:\\Users\\Bhoomi Swarnkar\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
            os.startfile(apath)

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir = "C:\\Users\\Bhoomi Swarnkar\\Music\\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            #for songs in songs:
                #if songs.endswith('.mp3'):
            os.startfile(os.path.join(music_dir,rd))


        elif "ip address"  in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("mam,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+919555392617", "this is testing protocol",13,43)

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")


        elif "email to bhoomi" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "bhoomi3051@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to bhoomi")

            except Exception as e:
                print(e)
                speak("sorry mam, i am not able to send this email")

        elif"no thanks" in query:
            speak("thanks for using me mam have a good day")
            sys.exit()

    #to close any application
        elif "close notepad" in query:
            speak("okay mam,closing notepad")
            os.system("taskkill /f /in notepad.exe")

    # to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = "C:\\Users\\Bhoomi Swarnkar\\Music\\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir),songs[0])

    #to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t s")

        elif "restart the system" in query:
            os.system("shutdown /r /t s")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait mam,fetching the latest news")
            news()


        speak("mam,do you have any other work")




