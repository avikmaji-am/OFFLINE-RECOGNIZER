<div align="center">

# 🎙️ OFFLINE RECOGNIZER
**The Elite, Privacy-First Speech-to-Text Engine**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Vosk](https://img.shields.io/badge/Vosk-Engine-FF6F00?style=for-the-badge)](https://alphacephei.com/vosk/)
[![Flask](https://img.shields.io/badge/Flask-Web_UI-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Privacy](https://img.shields.io/badge/Data-Encrypted_&_Local-success?style=for-the-badge)](/)

---



### "Zero cloud. Zero latency. Total control."

</div>


## ▶️ How To Run?

Installation :
1. pip install sounddevice  
2. pip install vosk
3. pip install pyttsx3
4. pip install Flask

Requirements : 
```bash

 pip install sounddevice  
 pip install vosk
 pip install pyttsx3
 pip install Flask

```



## 📦 Description (Used Modules) :

- **sounddevice :** Used to capture real-time audio input from the system microphone and stream it for processing.  

- **vosk :** An offline speech recognition engine used to convert spoken audio into text without using the internet.  

- **queue :** Used to safely store and transfer recognized text data between the audio callback function and the main program loop.  

- **json :** Used to parse and extract recognized text from the JSON output returned by the Vosk recognizer.  
- **Pyttsx3 :** pyttsx3 is a Python text-to-speech (TTS) library. It converts text into spoken audio using your computer’s built-in speech engines.  
- **Flask :**  Flask is a lightweight and flexible web framework for Python. It allows you to build web applications and APIs quickly without requiring complex setup. Flask is easy to learn and provides the essentials for web development, including routing, templates, and request handling.

---

## 📝 What It Does

- **OFFLINE RECOGNIZER** is a Python program that listens to your microphone and converts your speech into text in real-time—without requiring an internet connection.

---

## 🔑 Key Functions:

- **Real-Time Recognition :–** Captures your voice continuously and prints what you say almost instantly.

- **Offline Operation :–** Uses the Vosk speech recognition engine, so no cloud or internet is needed.

- **Phrase-Level Output :–** Instead of giving one letter at a time, it outputs complete words and phrases.

- **Easy Integration :–** Provides a Python generator (offline_recogniser()) that you can use in other projects.

---

---
## 🔗 Essential Resources

<div align="left">

| 📚 Core Technology | 🌐 Official Documentation |
| :--- | :--- |
| **Python** | [Official Website ↗](https://www.python.org/) |
| **Vosk Engine** | [Official Website ↗](https://alphacephei.com/vosk/) |
| **Vosk Models** | [All Models Download ↗](https://alphacephei.com/vosk/models) |
| **Vosk Model** | [Indian Version (Zip) ↗](https://alphacephei.com/vosk/models/vosk-model-en-in-0.5.zip) |
| **SoundDevice** | [Library Documentation ↗](https://python-sounddevice.readthedocs.io/) |
| **Queue** | [Data Management Docs ↗](https://docs.python.org/3/library/queue.html) |
| **JSON** | [Data Parsing Docs ↗](https://docs.python.org/3/library/json.html) |
| **Pyttsx3** | [TTS Documentation ↗](https://pypi.org/project/pyttsx3/) |
| **Flask** | [Web Framework Docs ↗](https://flask.palletsprojects.com/en/stable/) |

</div>

---

### ⚡ Quick Navigation Links
<p align="left">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /></a>
  <a href="https://alphacephei.com/vosk/"><img src="https://img.shields.io/badge/Vosk-Offline-FF6F00?style=for-the-badge" /></a>
  <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-Web-000000?style=for-the-badge&logo=flask&logoColor=white" /></a>
</p>
---

## 💬 Example Usage:

Speak: “Hello, how are you?”

# Output : 
```bash
✅ Recognized: hello world 
✅ Recognized: how are you
```

