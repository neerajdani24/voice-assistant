
# 🎙️ Voice Assistant using Python

This is a simple voice assistant project built using Python. It listens to your voice commands and performs a range of actions such as reading the news, telling jokes, providing weather updates, playing YouTube videos, and searching Wikipedia.

---

## 🚀 Features

- 🔊 Greets the user based on the time of day
- 🌦️ Provides real-time weather updates for Tumakuru
- 📰 Reads the latest news from WSJ (via News API)
- 🎥 Plays YouTube videos using Selenium
- 🧠 Fetches information from Wikipedia
- 😂 Tells random jokes
- 💡 Shares interesting random facts

---

## 🧰 Technologies Used

- Python 3.x
- SpeechRecognition
- pyttsx3 (Text-to-Speech)
- Selenium (Web Automation)
- `requests` (API calls)
- randfacts
- YouTube + Wikipedia (via browser automation)
- News API (https://newsapi.org)
- OpenWeatherMap API (https://openweathermap.org)

---

## 🔧 Project Structure

```
voice-assistant/
├── voice_assistant.py     # Main file to run the assistant
├── weather.py             # Fetches weather data
├── news.py                # Fetches news headlines
├── jokes.py               # Gets random jokes
├── YT_auto.py             # Automates YouTube search and play
├── selenium_web.py        # Fetches Wikipedia info
```

---

## ⚙️ Setup Instructions

1. **Clone this repository:**
   ```bash
   git clone https://github.com/neerajdani24/voice-assistant.git
   cd voice-assistant
   ```

2. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API keys:**
   - Replace the placeholder keys in `weather.py` and `news.py` with your actual API keys.

4. **Ensure ChromeDriver is installed:**
   - Download from: https://chromedriver.chromium.org/downloads
   - Update the `chromedriver.exe` path in `selenium_web.py` and `YT_auto.py`.

5. **Run the assistant:**
   ```bash
   python voice_assistant.py
   ```

---

## 📌 Requirements (Put this in `requirements.txt`)

```
requests
pyttsx3
SpeechRecognition
randfacts
selenium
```

---

## 🙋‍♂️ Author

- **Neeraj Dani**  
  [GitHub](https://github.com/neerajdani24)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
