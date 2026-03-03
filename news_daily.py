import requests
import time
import speech_recognition as sr
import webbrowser
import pyttsx3
from dotenv import load_dotenv
import os
load_dotenv()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)                 #converts text into speech
    print(text)
    engine.runAndWait()

newsapi= os.getenv("news_api")
r1 = sr.Recognizer()
def tell_News():
    r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
    if r.status_code == 200:
        #parse json response
        data = r.json()         #json data is structured data that is in the form of dictionaries & arrays.

        #extract articles
        articles = data.get('articles',[])
        if articles:
        #print the headlines
            for article in articles:
                speak(article['title'])
                time.sleep(1)           #pause for a moment before listening for commands

                # Listen for user commands while reading the news
                while True:
                    print("Listening for commands: 'ok, thanks' to stop or 'tell me more' or 'let me see' to continue.")

                    with sr.Microphone() as source:
                        r1.adjust_for_ambient_noise(source)  # Adjust for ambient noise
                        r1.pause_threshold=0.5

                        try:
                            command_audio = r1.listen(source,timeout=5,phrase_time_limit=3)  # Listen for the next command
                            command = r1.recognize_google(command_audio).lower()  # Recognize the command
                            print(f"command is:{command}")

                            if "ok thanks" in command:
                                speak("Okay, stopping the news.")
                                return  # Exit the function

                            elif "tell me more" in command:
                                speak("okay. another news is about..")
                                break  # Break the loop to read the next headline

                            elif "let me see" in command:
                                # Open the article URL in the web browser
                                webbrowser.open(article['url'])  # Open the specific article
                                speak("Opening the article for you.")
                                continue  # Continue listening for the next command


                        except sr.UnknownValueError:
                            speak("Sorry, I didn't catch that. Please repeat.")
                            continue  # Ask for the command again
                        except sr.RequestError:
                            speak("Could not request results from the speech recognition service.")
                            return  # Exit the function


        else:
            speak("No news articles found.")
    else:
        speak("Error fetching news!")

