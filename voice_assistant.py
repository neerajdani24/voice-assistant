import pyttsx3 as p
import speech_recognition as sr
from YT_auto import *
from selenium_web import *
from news import *
import randfacts
from jokes import *
from weather import *
import datetime

engine = p.init()
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Adjust index for your preferred voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour>8 and hour<12:
        return ("morning")
    elif hour>=12 and hour<16:
        return ("afternoon")
    else:
        return("evening")

today_date=datetime.datetime.now()
r = sr.Recognizer()

speak("Hello sir, good"+wishme()+", I'm your voice assistant. ")
speak("today is"+today_date.strftime("%d")+"of"+today_date.strftime("%B")+"And it is currently"+today_date.strftime("%I")+today_date.strftime("%M")+today_date.strftime("%p"))
speak("Temperature in Tumakuru is " +str(temp())+"degrees"+"and with"+str(des()))
speak("how are you")

class Infow:
    pass


def music():
    pass


try:
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)

    if "and" and "you" in text:
        speak("I am also having a good day, sir.")
    speak("What can I do for you?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        print(text2)

    if "information" in text2:
        speak("You need information about which topic?")

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = r.listen(source)
            infor = r.recognize_google(audio)
        speak("searching {} in wikipedia".format(infor))
        print("searching {} in wikipedia".format(infor))
        assist = infow()
        assist.get_info(infor)

        input("Press Enter to close the browser...")
        assist.close_browser()

    elif "play" and "video" in text2:
        speak("you want me to play which video?")
        with (sr.Microphone() as source):
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = r.listen(source)
            vid = r.recognize_google(audio)
            speak("Playing {} on youtube".format(vid))
            print("Playing {} on youtube".format(vid))
            if __name__ == "__main__":
                assist = Music()
                assist.play(vid)


        input("Press Enter to close the browser...")
        assist.close_browser()

    elif "news" in text2:
        print("sure sir,Now i will read news for you")
        speak("sure sir,Now i will read news for you")
        arr=news()
        for i in range(len(arr)):
            print(arr[i])
            speak(arr[i])

    elif "fact" or "facts" in text2:
        speak("sure sir")
        x=randfacts.get_fact()
        print(x)
        speak("Did you know that"+x)

    elif "jokes" or "jokes" in text2:
        speak("sure sir,")
        arr=joke()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])

except sr.UnknownValueError:
    speak("Sorry, I couldn't understand. Could you repeat?")
except sr.RequestError as e:
    speak(f"Speech recognition service error: {e}")
except Exception as e:
    speak(f"An error occurred: {e}")