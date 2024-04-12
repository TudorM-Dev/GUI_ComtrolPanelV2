import speech_recognition

recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            print("Ask me")
            audio=recognizer.listen(mic)    
            text=recognizer.recognize_google(audio)
            text = text.lower()
            print("Your command", text)

    except ex:
        # pass
        print("idk")
        recognizer = speech_recognition.Recognizer()
        continue
        

