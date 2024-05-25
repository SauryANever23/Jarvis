from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("temp.mp3")
    os.system("mpg321 temp.mp3")

# Example usage
speak("Hello, world!")
