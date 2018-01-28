#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

while True:
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


    # recognize speech using Google Speech Recognition
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    try:
        if(r.recognize_google(audio)=="forward"):
            print("forward it is")
        elif(r.recognize_google(audio)=="left"):
            print("left it is")
        elif(r.recognize_google(audio)=="right"):
            print("right it is")
        elif(r.recognize_google(audio)=="backward"):
            print("backward it is")
        elif(r.recognize_google(audio)=="stop"):
            exit(0)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

