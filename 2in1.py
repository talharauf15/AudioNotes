import streamlit as st
import whisper
import numpy as np
import sounddevice as sd
import queue
import tempfile
import os
import scipy.io.wavfile as wav

# Set page config first
st.set_page_config(page_title="AudioNotes", page_icon="🎤", layout="wide")

# Load the Whisper model (cached)
@st.cache_resource
def load_model():
    return whisper.load_model("base")  # Changed to standard "base" model ("turbo" isn't valid)

model = load_model()

# Audio recording parameters
samplerate = 44100  # Sample rate in Hz
channels = 1  # Mono recording
q = queue.Queue()

# ========== Shared Functions ==========


def transcribe_audio(file_path):
    """Transcribe audio using Whisper model"""
    result = model.transcribe(file_path)
    return result["text"]

# ========== Page Configuration ==========

st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Choose Mode", ["Live Recording", "File Upload"])

# ========== Live Recording Section ==========
if app_mode == "Live Recording":
    st.title("🎙️ Live Speech-to-Text")
    
    # Audio callback function
    def callback(indata, frames, time, status):
        if status:
            print(status)
        q.put(indata.copy())

    # Recording controls
    col1, col2 = st.columns(2)
    with col1:
        duration = st.number_input(
            "Recording Duration (seconds)", min_value=1, max_value=60, value=5
        )
    
    if col2.button("Start Recording 🎤"):
        st.write("Listening... Speak now!")
        
        # Start recording
        with sd.InputStream(callback=callback, channels=channels, samplerate=samplerate):
            sd.rec(int(samplerate * duration), samplerate=samplerate, channels=channels, dtype=np.int16)
            sd.wait()

        # Process audio data
        audio_data = np.concatenate([q.get() for _ in range(q.qsize())], axis=0)
        
        # Save temporary audio file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            wav.write(temp_audio.name, samplerate, audio_data)
            temp_path = temp_audio.name

        # Transcribe and display results
        st.write("Transcribing... ⏳")
        try:
            text = transcribe_audio(temp_path)
            st.subheader("Transcribed Text:")
            st.write(text)

            # Add download button for transcribed text
            st.download_button(
                label="Download Transcription",
                data=text,
                file_name="transcription.txt",
                mime="text/plain",
            )
        finally:
            os.remove(temp_path)

# ========== File Upload Section ==========
else:
    st.title("🎤 Audio File Transcription")
    st.write("Upload your audio file to transcribe it into text.")

    uploaded_file = st.file_uploader(
        "Choose audio file", type=["mp3", "wav", "m4a"], key="file_uploader"
    )
    
    if uploaded_file is not None:
        # Save to temporary file
        file_ext = uploaded_file.name.split(".")[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}") as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            temp_path = temp_file.name

        # Audio player and controls
        st.audio(temp_path, format=f"audio/{file_ext}")
        
        if st.button("Start Transcription"):
            st.write("Transcribing... ⏳")
            try:
                text = transcribe_audio(temp_path)
                with st.expander("Show Transcribed Text", expanded=True):
                    st.write(text)
                
                # Add download button for transcribed text
                st.download_button(
                    label="Download Transcription",
                    data=text,
                    file_name="transcription.txt",
                    mime="text/plain",
                )
            except Exception as e:
                st.error(f"Error transcribing file: {str(e)}")
            finally:
                os.remove(temp_path)
