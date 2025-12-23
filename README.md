# 🎙️ OFFLINE RECOGNIZER 

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

---

## 📦 Description (Used Modules) :

- **sounddevice :** Used to capture real-time audio input from the system microphone and stream it for processing.  

- **vosk :** An offline speech recognition engine used to convert spoken audio into text without using the internet.  

- **queue :** Used to safely store and transfer recognized text data between the audio callback function and the main program loop.  

- **json :** Used to parse and extract recognized text from the JSON output returned by the Vosk recognizer.  
- **Pyttsx3 :** pyttsx3 is a Python text-to-speech (TTS) library. It converts text into spoken audio using your computer’s built-in speech engines.  
- **Flask :**  Flask is a lightweight and flexible web framework for Python. It allows you to build web applications and APIs quickly without requiring complex setup. Flask is easy to learn and provides the essentials for web development, including routing, templates, and request handling.

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

## 🔗 Links
- ** 🔹 Python Official Website   :—** <https://www.python.org/>
- ** 🔹 Vosk Official Website     :—** <https://alphacephei.com/vosk/>
- ** 🔹 Vosk All Models Download  :—** <[https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)>
- ** 🔹 Vosk Model Indian Version :—** <[https://alphacephei.com/vosk/models/vosk-model-en-in-0.5.zip](https://alphacephei.com/vosk/models/vosk-model-en-in-0.5.zip)>
- ** 🔹 SoundDevice Documentation :—** <[[https://python-sounddevice.readthedocs.io/](https://pypi.org/project/sounddevice/](https://python-sounddevice.readthedocs.io/](https://pypi.org/project/sounddevice/)](https://pypi.org/project/sounddevice/)>
- ** 🔹 Queue Documentation       :—** <https://python-sounddevice.readthedocs.io/](https://pypi.org/project/sounddevice/](https://www.askpython.com/python-modules/python-queue>
- ** 🔹 Json Documentation       :—** <https://docs.python.org/3/library/json.html>
- ** 🔹 Pyttsx3 Documentation       :—** <https://pypi.org/project/pyttsx3/>
- ** 🔹 Flask Documentation       :—** <https://flask.palletsprojects.com/en/stable/>

## 💬 Example Usage:

Speak: “Hello, how are you?”

# Output : 
```bash
✅ Recognized: hello world 
✅ Recognized: how are you
```
