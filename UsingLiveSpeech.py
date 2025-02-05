import streamlit as st
import whisper
import numpy as np
import sounddevice as sd
import queue
import torch
import tempfile
import os
import scipy.io.wavfile as wav

# Load the Whisper model (use "base" or "small" for better speed)
@st.cache_resource
def load_model():
    return whisper.load_model("turbo")

model = load_model()

# Audio recording parameters
samplerate = 44100  # Sample rate in Hz
channels = 1  # Mono recording
q = queue.Queue()

# Function to continuously record audio
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(indata.copy())

# Function to transcribe audio
def transcribe_audio(audio_data):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        wav.write(temp_audio.name, samplerate, audio_data)
        try:
            result = model.transcribe(temp_audio.name)
        finally:
            temp_audio.close()  # Close the file to release it
            os.remove(temp_audio.name)  # Cleanup after closing the file
    return result["text"]

st.title("🎙️ Live Speech-to-Text using Whisper AI")

# Button to start recording
if st.button("Start Recording 🎤"):
    st.write("Listening... Speak now!")
    
    # Start recording with the correct parameters
    duration = 5  # Adjust duration as needed
    with sd.InputStream(callback=callback, channels=channels, samplerate=samplerate):
        sd.rec(int(samplerate * duration), samplerate=samplerate, channels=channels, dtype=np.int16)
        sd.wait()  # Wait for recording to finish

    # Convert queue data to numpy array
    audio_data = np.concatenate([q.get() for _ in range(q.qsize())], axis=0)

    # Transcribe audio
    st.write("Transcribing... ⏳")
    text = transcribe_audio(audio_data)

    # Display results
    st.subheader("Transcribed Text:")
    st.write(text)

