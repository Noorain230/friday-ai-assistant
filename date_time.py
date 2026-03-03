import datetime
import os
import time         #import time library for sleep functionality
import speech_recognition as sr
import pyttsx3
import re
engine = pyttsx3.init()

def speak(text):
    engine.say(text)                 #converts text into speech
    print(text)
    engine.runAndWait()

def tell_time():
    return datetime.datetime.now().strftime("%I:%M %p")


def set_alarm():
    recognizer = sr.Recognizer()
    try:
        speak("What time would you like to set the alarm for?")

        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5)
        time_str = recognizer.recognize_google(audio).lower()

        # Modified regular expression to make space optional
        match = re.search(r"(\d{1,2})(?::(\d{1,2}))?\s*(am|pm)?", time_str)
        if not match:
            raise ValueError("Invalid time format")
            speak("invalid time format")

        hour = int(match.group(1))
        minute = int(match.group(2)) if match.group(2) else 0
        am_pm = match.group(3)

        if am_pm == "pm" and hour != 12:
            hour += 12
        elif am_pm == "am" and hour == 12:
            hour = 0
        elif am_pm == None and datetime.datetime.now().hour > hour:
            hour += 12

        alarm_time = datetime.time(hour, minute)
        speak(f"Alarm set for {alarm_time.strftime('%I:%M %p')}.")

        while True:
            now = datetime.datetime.now().time()
            if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
                music_dir = "C:\\music"
                songs = os.listdir(music_dir)       #returns list of files and directories from the specified directory
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))  #joins path components, will go in music_dir and retrieves the first song and joins it. for eg= C:\\music\\song1.mp3
                    break
                else:
                    speak("No music files found in the specified directory.")
                    speak("time to wake up..")
                    break
            time.sleep(20)
    except sr.UnknownValueError:
        speak("Sorry, i didn't catch that. please try again.")

    except Exception as e:
        print(e)
        speak("an error occurred while setting the alarm.")
