# friday-ai-assistant
Friday Assistant is a JARVIS-inspired intelligent desktop system that integrates voice interaction with web services and system automation to enhance productivity and user experience. 
<br>
# Features <br>

### 🖥️ System Control
- Open Notepad
- Close Notepad
- Open Command Prompt
- Shutdown system
- Restart system
- Control system volume (up, down, mute)

### 🌐 Web & Application Control
- Open YouTube
- Open WhatsApp Web
- Search on Google
- Search on Wikipedia and read results
- Search products on Amazon

### 🎙️ Voice & Smart Assistance
- Voice command recognition
- Text-to-speech response
- Tell current time
- Set alarms
- Tell jokes
- Check temperature

### 🎵 Media & Utilities
- Play songs
- Take screenshots

---

## 🛠️ Technologies & Tools Used

### 🔹 Core Language
- Python

### 🔹 GUI Framework
- PyQt5

### 🔹 Voice Processing
- SpeechRecognition
- pyttsx3

### 🔹 Automation & System Control
- os
- datetime
- webbrowser
- pyautogui

### 🔹 APIs & Utilities
- wikipedia
- pyjokes
- News API
- python-dotenv

---

## 🔐 Environment Variables

This project uses a .env file to securely store API keys.

Create a .env file in the root directory and add:


NEWS_API_KEY=your_api_key_here


⚠️ Do not upload your .env file to GitHub.

---

## ▶️ How to Run

1. Clone the repository:


git clone https://github.com/your-username/friday-assistant.git


2. Navigate into the project folder:


cd friday-assistant


3. Install dependencies:


pip install -r requirements.txt


4. Create a .env file and add your News API key.

5. Run the project:


python main.py


---

## 📜 License

This project is licensed under the MIT License.

---

Developed by Noorain
