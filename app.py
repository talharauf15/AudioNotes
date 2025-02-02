import streamlit as st
import whisper
import os

# Load the Whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Streamlit UI
st.title("🎤 Speech-to-Text App using Whisper AI")

# File uploader
uploaded_file = st.file_uploader("Upload an audio file (MP3, WAV, M4A)", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    # Save the file locally
    file_path = "temp_audio." + uploaded_file.name.split(".")[-1]
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.audio(file_path, format="audio/mp3")  # Play uploaded audio

    # Transcribe the audio file
    st.write("Transcribing... ⏳")
    result = model.transcribe(file_path)

    # Display transcribed text
    st.subheader("Transcribed Text")
    st.write(result["text"])

    # Cleanup temporary file
    os.remove(file_path)
