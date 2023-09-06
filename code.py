import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning")

    elif 12 <= hour < 18:
        speak("Good afternoon")

    else:
        speak("Good evening")

    speak("How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again...")
        return "None"
    return query


if __name__ == "__main__":
    speak("Hello")
    wishme()
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            # Wikipedia search logic (unchanged)
            pass

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'play music' in query:
            # Music playback logic (unchanged)
            pass

        elif 'the time' in query:
            # Time retrieval logic (unchanged)
            pass

        else:
            # Open a web browser with a Google search for the user's query
            search_query = "https://www.google.com/search?q=" + query
            webbrowser.open(search_query)
