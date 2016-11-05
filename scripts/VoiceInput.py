#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

#import webhandler
import sys
sys.path.insert(0, '../')
from textparser import*

def GetVoice():
    r = sr.Recognizer()


    with sr.Microphone() as source:
        print("Say something: ")
        audio = r.listen(source)
    return audio

def GetText(audio):
    r = sr.Recognizer()
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`

        # r.recognize_google(
        # audio,
        # key="ya29.Ci-MA2OjZ4mBUqZS6RGtf3i8gUv0M_oLoc15xLHcf5xjbYLTjV0ZykDRYCfsukVEuQ")

        text = "No Input"
        text = r.recognize_google(audio)

    # TODO Remove
        print("Text: " + text)
    except sr.UnknownValueError:
        print("Engine could not process the speech")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))

    return text

    '''
def GetInput():
    # obtain audio from the microphone
    r = sr.Recognizer()


    with sr.Microphone() as source:
        print("Say something: ")
        audio = r.listen(source)


    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`

        # r.recognize_google(
        # audio,
        # key="ya29.Ci-MA2OjZ4mBUqZS6RGtf3i8gUv0M_oLoc15xLHcf5xjbYLTjV0ZykDRYCfsukVEuQ")

        text = "No Input"
        text = r.recognize_google(audio)

    # TODO Remove
        print("Text: " + text)
    except sr.UnknownValueError:
        print("Engine could not process the speech")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))

    return text
'''