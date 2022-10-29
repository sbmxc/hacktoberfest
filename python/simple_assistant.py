import pywhatkit as kit
import webbrowser
import screen_brightness_control as sbc
import asyncio
import platform
import keyboard
from typing import Hashable
from dataclasses import dataclass
import calendar
import datetime
import os
import sys
import subprocess
import webbrowser
import psutil
import requests
import re
import speech_recognition as sr
import pyttsx3
from difflib import SequenceMatcher

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#greets the user
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Good Morning Boss"
    elif 12 <= hour < 18:
        return "Good Afternoon Boss"
    else:
        return "Good evening Boss"


current_brightness = sbc.get_brightness()
battery = psutil.sensors_battery()
percent = battery.percent

engine = pyttsx3.init('sapi5')
rate = engine.getProperty("rate")
engine.setProperty("rate", 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak(wishMe())

@dataclass
class ActionInput(Hashable):
    def __hash__(self) -> int:
        return str(self.value).__hash__()

    value: list[str]

async def main():

    def there_exists(terms):
        for term in terms:
            if term in response or SequenceMatcher(None, response, term).ratio() > 0.85:
                return True

    #takes voice input from user    
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            sr.Recognizer().adjust_for_ambient_noise(source, duration=0.2)
            print("Listening...")
            audio = r.listen(source)

            try:
                response = r.recognize_google(audio, language='en-in')
                print(f"user said:{response}\n")

            except Exception as e:
                return "None"
            return response.lower()

    #stops the program
    def powerdown():
        speak("Nice talking with you")
        sys.exit(0)

    #opens a new chrome tab
    def google():
        webbrowser.open_new_tab("https://www.google.com")
        time.sleep(5)

    #opens gmail in a new tab
    def gmail():
        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
        time.sleep(5)

    #raises volume if param status is up and decreases volume if status is down
    def volume(status):
        if status == 'up':
            for i in range(3):
                pyautogui.press('volumeup')
                speak("Increased volume by 10 percent")
        elif status == 'down':
            for i in range(3):
                pyautogui.press('volumedown')
                speak("Decreased volume by 10 percent")

    #notes down input from the user in a text file    
    def notedown():
        speak("What do you want me to note down?")
        response = takeCommand()
        note(response)
        speak("I have made a note of that")

    #tells a joke
    def joke():
        joke = (pyjokes.get_joke())
        speak(joke)
        print(joke)

    #logs-off the pc
    def logoff():
        speak(
            "Your pc will log off in 10 sec make sure you exit from all applications")
        subprocess.call(["shutdown", "/l"])
            
    #shutsdown the pc        
    def shutdown():
        speak("Shutting down your pc, make sure you exit from all applications")
        subprocess.call(["shutdown", "/s"])

    #restarts the pc
    def restart():
        speak("Restarting your pc, make sure you exit from all applications")
        subprocess.call(["shutdown", "/r"])

    #changes brightness based on the param status
    def brightness(status):
        if status == 'increase':
            if sbc.get_brightness() == 100:
                speak("Brightness is already at max")
            else:
                brightness = sbc.set_brightness(current_brightness + 10)
                speak(f"Increased brightness by 10 percent")
        elif status == 'decrease':
            if sbc.get_brightness() == 0:
                speak("Brightness is already at 0")
            else:
                sbc.set_brightness(current_brightness - 10)
                speak(f"Decreased brightness by 10 percent") 

    #takes a screenshot and saves it
    def screenshot():
        image = pyscreenshot.grab()
        speak("Should I open the image?")
        response = takeCommand()
        if there_exists(['yes', 'show', 'show the screenshot']):
            image.show()
        else:
            speak("Ok")

    #gets the current day
    def getDay():
        today = datetime.datetime.now()
        date = today.strftime("%d %m %y")
        day = datetime.datetime.strptime(date, '%d %m %y').weekday()
        return calendar.day_name[day]

    #convert-list-to-string
    def listToString(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    #gets the current location
    def getLocation():
        res = requests.get("https://ipinfo.io/")
        data = res.json()
        city = data["city"].split(',')
        return listToString(city)

    #function-to-make-a-note
    def note(text):
        date = datetime.datetime.now()
        file_name = str(date).replace(':', '-') + "-note.txt"
        with open(file_name, "w") as f:
            f.write(text)

        sublime = paths.get(sublime)
        subprocess.Popen([sublime, file_name])

    #function-to-get-quick-answers from duckduckgo
    def getQuickAnswers(query):
        url = "https://api.duckduckgo.com"
        response = requests.get(url, params={"q": query, "format": "json"})
        data = response.json()
        final = ' '.join(re.split(r'(?<=[.])\s', data['Abstract'])[:2])
        if final == '':
            speak("Error, please try again later")
        else:
            return final

    #gets the current location
    def location():
        res = requests.get("https://ipinfo.io/")
        data = res.json()
        city = data["city"].split(',')
        state = data["region"].split(',')
        speak(f'You are in {city},{state}')
        print(f'You are in {city},{state}')

    while True:
        print("Listening..")
        response = takeCommand()

        def youtube():
            search_term = response.replace("play", '')
            kit.playonyt(search_term)
            speak(f"Playing {search_term}")

        def searchYoutube():
            search_term = response.replace("on youtube", '')
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on youtube')

        def search():
            search_term = response.split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on google')
            
        actions = {
            ActionInput(["close current tab", 'close tab']): (lambda: keyboard.press_and_release('ctrl+w')),
            ActionInput(['goodbye', 'bye', 'see you later', 'ok bye']): (lambda: powerdown()),
            ActionInput(['open google', 'open new tab in google', 'new tab in google']): (lambda: google()),
            ActionInput(['gmail', 'open gmail']): (lambda: gmail()),
            ActionInput(['whats the day today', 'what day is it today', 'day']): (lambda: speak(f'Today is {getDay()}')),
            ActionInput(['battery percentage', 'what is the battery like right now', 'tell me the battery percentage']): (lambda: speak("Current battery percentage is at" + str(percent) + "percent")),
            ActionInput(['what is the current brightness', 'current brightness', 'what is the brightness like right now']): (lambda: speak(str(sbc.get_brightness()) + "percent")),
            ActionInput(["current location", "location", "where am i", "where am I right now"]): (lambda: location()),
            ActionInput(['increase volume', 'volume up']): (lambda: volume('up')),
            ActionInput(['decrease volume', 'volume down']): (lambda: volume('down')),
            ActionInput(['play']): (lambda: youtube()),
            ActionInput(["on youtube"]): (lambda: searchYoutube()),
            ActionInput(['take a note', 'note', 'note this down', 'remember this', 'take this down']): (lambda: notedown()),
            ActionInput(['tell me a joke', 'not funny', 'make me laugh', 'joke', 'tell me another joke']): (lambda: joke()),
            ActionInput(['search for']): (lambda: search()),
            ActionInput(['what is the time now', 'what time is it', 'time']): (lambda: speak(f"the time is {datetime.datetime.now().strftime('%H:%M')}")),
            ActionInput(['sign out', 'log off']): (lambda: logoff()),
            ActionInput(['shutdown the pc', 'shutdown', 'shutdown the laptop']): (lambda: shutdown()),
            ActionInput(['restart', 'restart the pc', 'restart the laptop']): (lambda: restart()),
            ActionInput(['increase brightness', 'the brightness is low']): (lambda: brightness('increase')),
            ActionInput(['decrease brightness', 'dim', 'dim the laptop', 'dim the screen', 'the screen is too bright']): (lambda: brightness('decrease')),
            ActionInput(['take a screenshot', 'screenshot', 'capture the screen', 'take a photo of this']): (lambda: screenshot()),
            ActionInput(['what', 'who', 'why', 'where', 'when', 'which']): (lambda: speak(getQuickAnswers((response)))),
        }

        for key in actions:
            if there_exists(key.value):
                actions[key]()

asyncio.run(main())
time.sleep(3)