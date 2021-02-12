# Importing necessary packages
import speech_recognition as sr
import webbrowser
import pyaudio
import pyttsx3
import time
import random

# Initializing python text to speech and setting it's voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Creating speak function 
def speak(text):
    engine.say(text)
    engine.runAndWait()


# This is the initial words from our alexa...
initial_text = "Hello Harsh, I am your alexa. How can i help you"
speak(initial_text)

# from googletrans import Translator
from translate import translator

r = sr.Recognizer()

# Reply for how are you
how = "I am extremely well"
# Reply for who are you
who = "I am alexa, Harsh voice assistant"
# Motivational quotes
before_quote = 'Okk. This is the quote i have right now to motivate you'
quotes = ['Your limitation—it’s only your imagination.',
          'Push yourself, because no one else is going to do it for you.',
          'Sometimes later becomes never. Do it now.', 'Great things never come from comfort zones.',
          ' Dream it. Wish it. Do it.', 'Success doesn’t just find you. You have to go out and get it.',
          ' The harder you work for something, the greater you’ll feel when you achieve it.']


# translator = Translator()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening ....")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            command = text.lower()
            if 'alexa' in command:
                command_f = command
                if 'open' and 'youtube' in command_f:
                    webbrowser.open_new('https://www.youtube.com/')
                if 'open' and 'twitter' in command_f:
                    webbrowser.open_new('https://twitter.com/')
                if 'how' and 'you' in command_f:
                    speak(how)
                if 'who' and 'you' in command_f:
                    speak(who)
                if 'play' and 'music' in command_f:
                    webbrowser.open_new('https://gaana.com/playlist/tanmay5709-gannacom')
                if 'what' and 'time' in command_f:
                    seconds = time.time()
                    print(time.ctime(seconds))
                if 'open' and 'whatsapp' in command_f:
                    webbrowser.open_new('https://web.whatsapp.com/')
                if 'inspire' or 'motivate' in command_f:
                    speak(before_quote)
                    speak(quotes[random.randint(0, 8)])

    except:
        pass
    return command_f


def run_alexa():
    comd = take_command()
    return comd


a = run_alexa()
