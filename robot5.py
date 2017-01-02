# import RPi.GPIO as gpio
import time
import sys
import os
from lib.Rover import Rover
from lib.sensor import distance
import random
import speech_recognition as sr



def callback(recognizer, audio):
    # try:
    #     print recognizer.recognize_google(audio)
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Google Speech Recognition service; {0}".format(e))

    try:
        rover_voice_control(r.recognize_ibm(audio, username=USERNAME, password=PASSWORD))
    except sr.UnknownValueError:
        print "IBM Speech to Text could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from IBM Speech to Text service; {0}".format(e)

def rover_voice_control(transcript):
    commands = transcript.split(' and ')
    for command in commands:
        if 'stop' in transcript: 
            rover.stop(.050) 
        elif 'go' in transcript or 'move' in transcript:
            rover.forward(.050)
        elif 'turn' in transcript:
            if 'right' in transcript: 
                rover.turn_right(.050)
            elif 'left' in transcript:
                rover.turn_left(.050)
        elif 'rotate' in transcript: 
            if 'right' in transcript:
                rover.pivot_right(.050)
            elif 'left' in transcript:
                rover.pivot_left(.050)

if __name__ == '__main__':
    for z in range(10):
        rover = Rover()
        rover.forward(.030)
    rover.stop(.030)
    
    # r = sr.Recognizer()
    # m = sr.Microphone(device_index=0, sample_rate=512, chunk_size=256)
    # # print m.list_microphone_names()
    # # import pyaudio
    # # for i in range(5):
    # #     print pyaudio.PyAudio().get_device_info_by_index(i)

    # with m as source:
    #     # we only need to calibrate once, before we start listening
    #     r.adjust_for_ambient_noise(source) 

    # print("Give Rover Commands!")
    # USERNAME = os.environ['WATSON_STT_USERNAME']
    # PASSWORD = os.environ['WATSON_STT_PASSWORD']
    # print "Bluemix Transcription: "

    # audio = r.listen_in_background(m, callback)

    # while True:
    #     continue
        