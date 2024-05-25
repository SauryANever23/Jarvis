import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
# making our AI speak
def speak(audio):
    pass