import pyttsx3
from easygui import *
import sys
fieldNames = ["Text"]
def speak():
        speak = multenterbox(msg=' Enter the text to Speek.', title='Enter',fields=(fieldNames))
        engine = pyttsx3.init()
        engine.setProperty('rate', 120)
        engine.say(speak)
        engine.runAndWait()
speak();
