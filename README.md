**📌 Speech-to-Text & Translation App - Documentation**
**Project Overview**
This Streamlit application enables users to:

Upload an audio file (mp3, wav, ogg, flac).
Transcribe speech-to-text using an AI-based model.
Detect the language of the transcribed text.
Translate the text into a user-selected language.
Convert the translated text into speech (TTS) for audio playback.

**Code Structure**
The app is structured as follows:

/speech-to-text-app
│── app.py                # Main Streamlit application
│── utils.py              # Utility functions (transcription, translation, etc.)
│── requirements.txt      # Dependencies for deployment
│── nao-medical.png       # Favicon for the app
│── .gitignore            # Ignore unnecessary files
└── README.md             # Documentation

📜 app.py (Main Application)
Handles the Streamlit UI, file uploads, session management, and AI integration.

**Imports & Setup**
Imports necessary libraries (streamlit, asyncio, gtts, os).
Sets page configuration (title, layout, and favicon).

**Session State Initialization**
Stores session data (transcription, translated_text, detected_lang, etc.).

**File Upload**
Accepts audio files (mp3, wav, ogg, flac).

**Transcription**
Calls transcribe_audio() from utils.py to generate text from speech.
Stores the transcribed text in st.session_state.

**Language Selection**
User selects a target language for translation.

**Translation**
Calls translate_text() from utils.py.
Displays translated text in st.session_state.

**Text-to-Speech (TTS)**
Uses gTTS to generate an audio file from the translated text.
Plays the translated audio in Streamlit.

🛠 utils.py (Utility Functions)
This file contains the AI functionalities used in the app.

1️⃣ transcribe_audio(audio_file)
Uses Deepgram API or Whisper AI to transcribe the uploaded audio.
Returns:
transcription → The converted text.
detected_lang → Language detected in the audio.
norm_lang → Normalized language name.

2️⃣ translate_text(text, source_lang, target_lang)
Uses Google Translate API or another translation model.
Converts text from source_lang to target_lang.
Returns:
translated_text → The translated sentence.

3️⃣ LANG_MAP
A dictionary mapping languages for selection (e.g., {"English": ["en"], "French": ["fr"]}).

**3️⃣ AI Tools Used**
This app relies on three AI-powered tools:

**Feature	Tool Used**
Speech-to-Text:	Deepgram API / Whisper AI
Translation:	Google Translate API
Text-to-Speech:	gTTS (Google Text-to-Speech)
