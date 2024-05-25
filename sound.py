from gtts import gTTS
import os

def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("temp.mp3")
    os.system("mpg321 temp.mp3")

# Example usage
speak("", lang='fr')  # Speaking in French
