import speech_recognition as sr

def test_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please say something:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("You said: " + r.recognize_google(audio))
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_microphone()