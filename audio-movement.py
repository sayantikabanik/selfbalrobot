#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyttsx3
import os

def speak(text):
    print(text)
    engine = pyttsx3.init()
    engine.say(str(text))
    engine.runAndWait()
# obtain audio from the microphone

def speechGoogle(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

        try:
            print("You said " + r.recognize_google(audio))
            return r.recognize_google(audio)
           
        except sr.UnknownValueError:
            speak("Could not understand audio . Please repeat")

    # recognize speech using Google Speech Recognition

    
       
def recognise():
    command_words = ["forward", "backward","left","right","stop"]
    command = speechGoogle()
    if command == None:
        main()
    else:
        words = command.split()
        if "forward" in words:
            print("forward it is")
            speak("moving forward")
            main()
        elif "left" in words:
            print("left it is")
            speak("moving left")
            main()
        elif "right" in words:
            print("right it is")
            speak("moving right")
            main()
        elif "backward" in words:
            print("backward it is")
            speak("moving back")
            main()
        elif "stop" in words:
            print("stop it is")
            speak("Good Bye")
            exit(0)
def main():
    while online == True:
        listen = speechGoogle()
        if listen== None:
            main()
        else:
            heard = listen.split()
        recognise()
        main()



online = True
main()

   
