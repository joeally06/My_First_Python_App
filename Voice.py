import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def greetings(text):
    tts = gTTS(text=text, lang='en', slow=True)
    filename = "Greetings.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def chess(text):
    tts = gTTS(text=text, lang='en', slow=True)
    filename = "game_chess.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

#def main():
playsound.playsound("Greetings.mp3")

text = get_audio()

if 'war' in text:
        chess("Wouldn't you rather play a nice game of Chess?")


#if __name__ == '__main__':
    #main()