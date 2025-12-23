# OFFLINE_RECOGNIZER.py
from flask import Flask, render_template, Response
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
from queue import Queue
import pyttsx3
import threading
import time

# ---------------------------
# Initialize Flask app
# ---------------------------
app = Flask(__name__)

# ---------------------------
# Audio settings
# ---------------------------
SAMPLE_RATE = 16000   # Microphone sample rate
BLOCK_SIZE = 8000     # Audio block size processed per callback

# ---------------------------
# Load Vosk model
# ---------------------------
model_path = r"C:\Users\Avik Maji\Desktop\vosk-model-en-in-0.5\vosk-model-en-in-0.5"
model = Model(model_path)

# ---------------------------
# Initialize TTS engine
# ---------------------------
def speak(text):
    """Speak the given text using pyttsx3"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Speech speed
    engine.say(text)
    engine.runAndWait()

# ---------------------------
# Create recognizer
# ---------------------------
rec = KaldiRecognizer(model, SAMPLE_RATE)
rec.SetWords(True)

# ---------------------------
# Queue for sending recognized text to browser
# ---------------------------
q = Queue()

# ---------------------------
# Audio callback function
# ---------------------------
def callback(indata, frames, time_info, status):
    """Process each audio block"""
    if status:
        print(status)
    if rec.AcceptWaveform(bytes(indata)):  # Returns True only when a phrase is complete
        result = json.loads(rec.Result())
        text = result.get("text", "").strip()
        if text:  # Only send full phrases
            q.put(text)


# ---------------------------
# Function to run audio stream in a separate thread
# ---------------------------
def audio_stream():
    """Continuously capture audio and process it with Vosk recognizer"""
    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
        dtype='int16',
        channels=1,
        callback=callback
    ):
        sd.sleep(int(1e8))  # Keep stream running indefinitely

# Start audio stream in a background thread
threading.Thread(target=audio_stream, daemon=True).start()

# ---------------------------
# Generator function to stream recognized text to browser
# ---------------------------
def gen():
    """Generator function to send recognized text every 1 second"""
    speak("Please Say Something")
    while True:
        # Collect text for 1 second
        text_to_send = None
        start_time = time.time()
        while time.time() - start_time < 1:
            if not q.empty():
                text = q.get()  # Get the next recognized phrase
                text_to_send = text  # Only keep the **latest** phrase in this interval
        # Send to browser if new phrase exists
        if text_to_send:
            yield f"data:{text_to_send}\n\n"


# ---------------------------
# Flask route: serve HTML page
# ---------------------------
@app.route('/')
def index():
    return render_template('index.html')  # HTML in templates/index.html

# ---------------------------
# Flask route: stream recognized text
# ---------------------------
@app.route('/stream')
def stream():
    return Response(gen(), mimetype='text/event-stream')

# ---------------------------
# Run Flask server
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
