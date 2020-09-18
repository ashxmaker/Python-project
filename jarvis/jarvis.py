import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am your python assistance How may I help you.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Getting it....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recoginizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        return "NONE"

    return query


if __name__ == '__main__':
    wishMe()

    if 1:
        query = takeCommand().lower()

        # logic for executing tasks on query
        if "hello" in query:
            speak("Hello")
            speak("I can open youtube,\tgoogle,\tsearch on wikipedia,\tplay music,\tshow time\n and many more for you......\nJust say it.")

        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to the sources of wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "open python code" in query:
            code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(code_path)

        elif "time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(str_time)
            speak(str_time)

        else:
            exit()