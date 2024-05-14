import speech_recognition as sr
import pyttsx3
import time

def listen(timeout=10):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=timeout)
            return r.recognize_google(audio)
        except sr.WaitTimeoutError:
            return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

duration_seconds = 5
starttime = time.time()

while True:
    time_passed = time.time() - starttime
    if time_passed >= duration_seconds:
        break
    
    command = listen().lower()
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "goodbye" in command or "bye" in command:
        speak("Goodbye!")
        break
    elif command:
        speak("I'm sorry, I didn't understand that command.")

