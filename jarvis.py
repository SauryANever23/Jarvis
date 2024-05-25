import speech_recognition as sr
import openai
import wikipedia
import os

def say(text):
    os.system(f"say {text}")

say("hello")    