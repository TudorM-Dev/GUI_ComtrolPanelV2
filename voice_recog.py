import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Init the mic...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Ask me")
        recordedAudio=recognizer.listen(source)

    try:
        command=recognizer.recognize_google_cloud(recordedAudio)
        print("Your command", command)
    except Exception as ex:
        print(ex)

            # if 'hello' in command:
            #     diag = "hi Tudor my master of the greates, just like Kanye West or Ye"
            #     engine.say(diag)
            #     engine.runAndWait()


cmd()


