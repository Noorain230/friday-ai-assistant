
import os  #built-in module that provides way to interact with os. makes code platform independent
import sys  #to exit the system
import datetime
import pyautogui                 #python library used for automating mouse and keyboard actions
import speech_recognition as sr  #used to recognize user's voice, supports various services like google, azure, amazon etc
import webbrowser  #opens urls in default web browser (urls like google,youtube, etc)
import musiclibrary
from date_time import tell_time
from date_time import set_alarm
from news_daily import tell_News
import pyjokes  #need to install it to use this module which contains random jokes
import random  #used to generate random numbers, choices from seq etc
import urllib.parse  #it is module used to manipulate and parse urls
import pyttsx3
#pyqt5 used to design and implement gui. pyqt5 contains tools in which we get Qtdesigner by which we can design gui and code is written for functionality
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from fridayUI import Ui_FRIDAY_AI_ASSISTANT
from bs4 import BeautifulSoup
import wikipedia       #this package simplifies the process of accessing and retrieving info from wikipedia without having to open wikipedia.org
import requests

recognizer = sr.Recognizer()  #will recognize the speech , helps in recognition functionality, returns recognized text
engine = pyttsx3.init()           #pyttsx3 will be initialized


def speak(text):
    engine.say(text)  #friday will be able to speak through it
    print(text)
    engine.runAndWait()  #wait until speaking is finished, then continues executing next line of code



#class mainThread inherits from Qthread for handling threads(which are flow of process : tasks).
#Qthread is used to create and manage threads in pyqt5 app. threads allows to perform tasks concurrently.
#using threads can help keep the UI responsive, without it UI gets freeze or become unresponsive when performing tasks.
class MainThread(QThread):
    def __init__(self):
       super(MainThread, self).__init__()

    #will run automatically when start() is called on a Qthread (or any Qthread object)
    def run(self):
        self.taskexecution()



    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:  # with=opens a resource(file,conn,etc)
            print("listening")
            #print("Recognizing...")
            r.adjust_for_ambient_noise(source)  #reduces bg noise and focuses on user's voice
            r.pause_threshold = 0.6  #maximum time of the silence before recognizer take it as end of the phrase.
            audio = r.listen(source, timeout=6,phrase_time_limit=4)  #source= will listen through specified source, timeout= waits for user to speak before giving up, phrase time limit= time limit for a single phrase

        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"\nuser said: {query}")

        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return "none"

        except Exception as e:
            print(f"error: {e}")
            return "none"

        return query


    def taskexecution(self):
        wish()
        while True:
            self.query = self.takecommand().lower()


            if "google" in self.query:  # if ask to open google,facebook,instagram,YouTube,whatsapp
                speak("what should i search for")
                cm = self.takecommand().lower()
                speak(f"searching Google for {cm}")
                url = f"https://www.google.com/search?q={cm}"
                webbrowser.open(url)

            elif "open notepad" in self.query:
                path = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2112.32.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
                speak("opening notepad")
                os.startfile(path)  #opens a file which path is specified

            elif "wikipedia" in self.query:
                speak("let me search..")
                query = self.query.replace("wikipedia",
                                           "")  # it modifies query var by removing the word "wikipedia" and replacing it with empty string.
                # eg : 'search in wikipedia for python' it will modify it to "search for python"
                result = wikipedia.summary(query, sentences=2)  # modified query, only returns first 2 sentences
                speak("as per wikipedia")
                sentences = result.split('.')
                for sentence in sentences:
                    speak(sentence)

            elif "open command prompt" in self.query:
                speak("opening command prompt")
                os.system("start cmd")  #open the cmd

            elif "product" in self.query:
                speak("okay, searching now..")
                #cleans up query and turns it into special code that website understands and includes it into amazon search address to show the exact results.
                query = self.query.replace("products",
                                           "").strip()  # remove products word and any leading/trailing spaces.
                if query:
                    encoded_query = urllib.parse.quote(query)  # encode the query into specialized format.
                    amazon_url = f"https://www.amazon.com/s?k={encoded_query}"  # /s indicates search , ?k is the query parameter that specifies the search term.
                    speak("here are the top results!")
                    webbrowser.open(amazon_url)
                else:
                    speak("Please specify what products you want to search for.")
                    continue

            elif "open youtube" in self.query:
                speak("opening youtube")
                webbrowser.open("https://youtube.com")

            elif "open whatsapp" in self.query:
                speak("opening whatsapp")
                webbrowser.open("https://whatsapp.com")

            elif self.query.startswith("play"):
                speak("playing the song")
                song = self.query.split(" ")[1]  # this will split "play songname" into list such as [play,songname] and will play index 1 value
                link = musiclibrary.music[song]
                webbrowser.open(link)

            elif "hello friday" in self.query:
                speak("yes. what can i do for you")
                continue

            elif "time" in self.query:
                speak(f"the current time is {tell_time()}")

            elif "news" in self.query:
                tell_News()

            elif "set alarm" in self.query:
                set_alarm()

            elif "joke" in self.query:
                speak("here's the joke.")
                jokes = pyjokes.get_jokes()  #get list of jokes
                if jokes:  #check if there are jokes in the list
                    joke = random.choice(jokes)  #selects random joke(element) from the list or tuple
                    speak(joke)
                else:
                    speak("couldn't find any at the moment")

            elif "shut down the system" in self.query:
                speak("system will be shutdown in few seconds")
                os.system("shutdown /s /t 5")  #initiates shutdown,/s specifies the pc should be shutdown,/t sets the timer, in this case the timer is set for 5sec sets a 5 sec and user will get a warning msg

            elif "restart the system" in self.query:
                speak("system is going to restart in few seconds")
                os.system("shutdown /r /t 5")  #same for this but it initiates restart

            # to close notepad or any other application
            elif "close notepad" in self.query:
                speak("okay. closing notepad")
                os.system("taskkill /f /im Notepad.exe")  #taskkill for terminating process, /f to force the termination even it is unresponsive or has unsaved date, im stands for image name of the app that should be targeted for termination.

            elif "increase" in self.query:
                speak("increasing the volume..")
                pyautogui.press("volumeup")     #it has built-in knowledge of media keys like "volumeup" and al;

            elif "decrease" in self.query:
                speak("decreasing the volume")
                pyautogui.press("volumedown")

            elif "mute" in self.query:
                speak("okay. it's muted")
                pyautogui.press("volumemute")

            elif "take a screenshot" in self.query:
                speak("taking a screenshot..")
                ss = pyautogui.screenshot()     #takes the ss of the entire screen and returns a PIL image object(pil or pillow is the python image library),
                ss.save("ss.jpg")               #saving the pil image as jpg :: saves the ss to ss.jpg file and the file will be saved in the current working directory(this).
                speak("Screenshot saved successfully.")

            elif "temperature" in self.query:
                speak("let me check it..")
                search = "temperature in nashik"
                url = f"https://www.google.com/search?q={search}"          #?q= indicates search query parameter
                webbrowser.open(url)
                """req = requests.get(url)                                    #used requests library to send http get request to the constructed url. and request.get() retrieves html content from google search pages
                data = BeautifulSoup(req.text, "html.parser")      #used beautifulsoup library handles content of the webpage that the url points to.  to parse html content of the search results page. req.text contains html content of the page, and specifies html parser to use which extracts relevant info by analyzing the page
                temp = data.find("div", class_="BNeawe").text        #searches for html for a div with a class attr. as div typically contains temp info in google search results
                speak(f"the current {search} is {temp}")
                """

            elif "that's enough" in self.query or "no thanks" in self.query:
                speak("Are you sure you want to exit?")
                confirmation = self.takecommand().lower()
                if "yes friday" in confirmation:
                    speak("okay, have a nice day")
                    sys.exit()
                else:
                    speak("Okay, I will continue.")

            speak("do you have any other work")



def wish():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"the current time is {current_time}")

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning")
        speak("Friday here. how can i assist you?")

    elif hour > 12 and hour < 18:
        speak("good afternoon")
        speak("Friday here. how can i assist you?")

    else:
        speak("good evening")
        speak("Friday here. how can i assist you?")



#object of class
startExecution = MainThread()


#class Main inherits from QMainWindow, which is a base class in pyqt5 for creating main app windows, which have menus, toolbars, labels, button etc
class Main(QMainWindow):
    def __init__(self):
        super().__init__()      #imp to properly initialize main window
        self.ui = Ui_FRIDAY_AI_ASSISTANT()  #creating object of fridayUI
        self.ui.setupUi(self)    #setup widgets and properties within the main window

        self.ui.pushButton.clicked.connect(self.starttask)  #it is connected to startTask()
        self.ui.pushButton_2.clicked.connect(self.close)  #close the window

        self.timer_label_6 = QTimer(self)                      #QTimer is used to create timers that trigger events at regular interval
        self.timer_label_6.timeout.connect(self.move_label_6)  #connected to move_label_4()
        #self.original_x = 0     #represents leftmost edge of the parent widget (the main window)
        self.direction = -1      # 1 means movement will be in positive x-direction that is towards right and -1 for -ve x direction (left)


    def starttask(self):
        self.ui.movie = QtGui.QMovie("../../../Downloads/4NB4.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../../Downloads/7AMX.gif")     #QMovie is used to display animated gif in pyqt5
        self.ui.label_2.setMovie(self.ui.movie)  #setting QMovie obj in the label widget
        self.ui.movie.start()  #it will start the animation of the file

        self.ui.movie = QtGui.QMovie("../../../Downloads/W9dC.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../../Downloads/output-onlinegiftools.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../../Downloads/Jarvis_Loading_Screen.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()



        timer = QTimer(self)        #tcreated QTimer object which tells the application to do something at regular intervals like update clock, move an object, after every 1000ms=(1)s
        timer.timeout.connect(self.showtime)    #timeout signal will call showTime() when timer's time is out (completed) to update the clock again.
        timer.start(1000)           #starts the timer

        startExecution.start()

        self.original_x = self.ui.label_6.x()  #stores the original x cord
        self.timer_label_6.start(100)  #start moving label_4 with 100 ms(0.1ms) interval



    def showtime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')      #converting QTime obj into string for human-readability, cause it contains hex or dec time values
        label_date = current_date.toString(Qt.ISODate)      #same for QDate , ISODate format is YYYY_MM_DD international standard that defines date and time
        self.ui.textBrowser_4.setText(label_time)             #setText = fetches current D&T and displays the updated info
        self.ui.textBrowser_5.setText(label_date)


    #responsible for moving the label_4
    def move_label_6(self):
        max_offset = 85                         #it represents the max distance(in px) that the label_4 can move from its original x-coord
        current_x = self.ui.label_6.x()             #x() gets the horizontal position of a widget
        if current_x <= self.original_x - max_offset:
            self.direction = 1
        elif current_x >= self.original_x:
            self.direction = -1  #reverse direction
        new_x = current_x + (5 * self.direction)          #adjust speed by changing 5px, if it 1 than the result is 5, means widget will move to 5 px towards right, if it is -1 than the result will be -1 so it will move 5px towards left
        self.ui.label_6.move(new_x, self.ui.label_6.y())  #y() is used to keep the current vertical position while changing its horizontal position.



app = QApplication(sys.argv)          #initialzes pyQt5 application allowing it to run and handle the events like button clicks, showtime, move label etc and it is imp step.
friday = Main()         #creates an instance of a class(pyqt5)
friday.show()           #shows the window
exit(app.exec_())       #app.exec starts the event loop of the app, exit() = exits the app

