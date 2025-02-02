
import streamlit as st
import whisper
import os

# ✅ Move this line to the first Streamlit command
st.set_page_config(page_title="AudioNotes", page_icon="🎤", layout="wide")

# Load the Whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("turbo")

model = load_model()

# Sidebar for file upload
st.sidebar.title("Upload Audio")
uploaded_file = st.sidebar.file_uploader("Upload an audio file (MP3, WAV, M4A)", type=["mp3", "wav", "m4a"])

# Main Content Area
st.title("🎤 AudioNotes (Speech-to-Text App using Whisper AI)")
st.write("Upload your audio file to transcribe it into text.")

if uploaded_file is not None:
    # Save the file locally
    file_path = "temp_audio." + uploaded_file.name.split(".")[-1]
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.audio(file_path, format="audio/mp3")  # Play uploaded audio

    # Transcribe the audio file
    if st.button("Start Transcription"):
        st.write("Transcribing... ⏳")
        result = model.transcribe(file_path)

        # Show the transcribed text in an expander
        with st.expander("Show Transcribed Text"):
            st.write(result["text"])

    # Cleanup temporary file
    os.remove(file_path)
