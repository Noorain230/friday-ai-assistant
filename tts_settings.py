import pyttsx3

def set_voice():
    engine = pyttsx3.init()     #tts engine is used convert predefined text into speech
    voices = engine.getProperty('voices')  #returns list of voice object, each representing diff voice available on the system.
    engine.setProperty('voice', voices[0].id)       #setting male voice
    return engine