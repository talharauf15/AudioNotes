# 🎧 AudioNotes - Audio Transcription App with Whisper AI

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI Whisper](https://img.shields.io/badge/OpenAI_Whisper-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/research/whisper)

AudioNotes is a user-friendly web application for converting speech in audio files to text using OpenAI's Whisper speech recognition model.

![image](https://github.com/user-attachments/assets/3525f0de-d234-49f4-9b9b-e490dbb8db5e)


## ✨ Features

- 🎵 Supports WAV, MP3, and MP4 audio formats
- ⚡ Real-time transcription using AI
- 🔊 Built-in audio player for original file playback
- 🎨 Simple and intuitive Streamlit interface
- 🤖 Powered by OpenAI's Whisper (base model)
- 📥 Download transcriptions as text files

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- FFmpeg (required by Whisper)

**Install FFmpeg:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# MacOS
brew install ffmpeg

# Windows (via chocolatey)
choco install ffmpeg
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/talharauf15/AudioNotes.git
cd AudioNotes
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the application locally:
```bash
python -m streamlit run FileName.py
```

## 🛠️ How to Use

1. Navigate to the application in your browser.
2. Choose between "Live Recording" or "File Upload" modes.
3. Record audio or upload a file in supported formats.
4. Click "Start Transcription" to generate text.
5. Download the transcribed text as a `.txt` file.

## 📚 Tech Stack

- **Python** (Primary language)
- **Streamlit** (Web interface)
- **OpenAI Whisper** (Speech recognition engine)
- **FFmpeg** (Audio processing)

## 🌟 Roadmap

- [ ] Multilingual transcription support
- [ ] Live audio transcription extension
- [ ] Browser extension development
- [ ] Support for larger Whisper models
- [ ] Enhanced UI with progress indicators

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Special thanks to OpenAI for creating the Whisper model
- Streamlit for the amazing app framework

## ⚠️ Note

- The small Whisper model has moderate accuracy. Consider using larger models for production.
- Audio files are processed locally (no cloud storage).
- Maximum file size is limited by Streamlit's uploader constraints.

---

📄 **License**  
MIT License - See [LICENSE](LICENSE) for details.
