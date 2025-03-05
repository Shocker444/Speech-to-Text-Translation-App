# 🗣️ Speech-to-Text & Translation App

![Streamlit](https://img.shields.io/badge/Streamlit-App-red) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Status](https://img.shields.io/badge/Status-Active-success)

## 📌 Table of Contents
- [📖 Overview](#-overview)
- [🚀 Features](#-features)
- [📂 Project Structure](#-project-structure)
- [⚙️ Installation](#%EF%B8%8F-installation)
- [💻 Usage](#-usage)
- [🛠️ AI Tools Used](#%EF%B8%8F-ai-tools-used)
- [🚀 Deployment](#-deployment)

---

## 📖 Overview
This **Streamlit** application allows users to:
1. **Upload an audio file** (`mp3`, `wav`, `ogg`, `flac`).
2. **Transcribe speech-to-text** using an AI-based model.
3. **Detect the language** of the transcribed text.
4. **Translate the text** into a user-selected language.
5. **Convert the translated text into speech (TTS)** for audio playback.

---

## 🚀 Features
✅ Speech-to-Text Transcription  
✅ Auto-detect Language  
✅ Translate Text to Any Language  
✅ Convert Translated Text to Speech  
✅ Secure File Upload & Processing  
✅ Easy-to-use Web Interface (Streamlit)

---

## 📂 Project Structure
```
/speech-to-text-app
│── app.py                # Main Streamlit application
│── utils.py              # Utility functions (transcription, translation, etc.)
│── requirements.txt      # Dependencies for deployment
│── nao-medical.png       # Favicon for the app
│── .gitignore            # Ignore unnecessary files
└── README.md             # Documentation
```

---

## ⚙️ Installation
### 🔹 Prerequisites
- Python 3.8+
- Pip installed

### 🔹 Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/speech-to-text-app.git
cd speech-to-text-app

# Install dependencies
pip install -r requirements.txt
```

---

## 💻 Usage
```bash
streamlit run app.py
```
Then open **http://localhost:8501/** in your browser.

---

## 🛠️ AI Tools Used
| **Feature**        | **Tool Used**                  |
| ------------------ | ------------------------------ |
| **Speech-to-Text** | `Deepgram API` / `Whisper AI`  |
| **Translation**    | `Google Translate API`         |
| **Text-to-Speech** | `gTTS (Google Text-to-Speech)` |


## 🚀 Deployment
You can deploy the app on **Streamlit Cloud, Heroku, AWS, or Render**.

### 🔹 Deploy on Streamlit Cloud
```bash
git push origin main  # Push your code to GitHub
```
Then, go to [Streamlit Cloud](https://share.streamlit.io/) and connect your GitHub repository.

### 🔹 Deploy on Render
1. Create a new **Web Service**.
2. Set **Build Command**: `pip install -r requirements.txt`
3. Set **Start Command**: `streamlit run app.py`

---

🚀 **Happy Cloning!**

