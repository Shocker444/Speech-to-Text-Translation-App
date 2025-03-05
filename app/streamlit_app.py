import streamlit as st
import asyncio
import os
from gtts import gTTS
from utils import LANG_MAP, translate_text, transcribe_audio

st.set_page_config(page_title='Speech-to-Text & Translation App', layout='centered', page_icon='app/nao-medical.png')

st.title('Speech-to-Text & Translation App')
st.write('This app transcribes audio files and translates text to different languages.')

# Initialize session state variables if they don't exist
if "transcription" not in st.session_state:
    st.session_state.transcription = None
if "detected_lang" not in st.session_state:
    st.session_state.detected_lang = None
if "norm_lang" not in st.session_state:
    st.session_state.norm_lang = None
if "translated_text" not in st.session_state:
    st.session_state.translated_text = None
if "target_lang" not in st.session_state:
    st.session_state.target_lang = None

uploaded_file = st.file_uploader("Choose an audio file", type=['mp3', 'wav', 'ogg', 'flac'])

if uploaded_file:
    if st.button("Transcribe", type="primary"):
        try:
            transcription, detected_lang, norm_lang = transcribe_audio(uploaded_file)
            
            # Store values in session state
            st.session_state.transcription = transcription
            st.session_state.detected_lang = detected_lang
            st.session_state.norm_lang = norm_lang
            st.session_state.translated_text = None  # Reset translation when a new transcription is made
            
        except Exception as e:
            st.error(f"Error during transcription: {e}")


# Always display transcription if available (even after a refresh)
if st.session_state.transcription:
    st.write("**DETECTED LANGUAGE:**", st.session_state.norm_lang)
    st.write("**TRANSCRIPTION:**", st.session_state.transcription)

    # Keep the language selection visible
    LANG_LIST = list(LANG_MAP.keys())
    target_lang = st.selectbox("Select target language for translation:", LANG_LIST, index=None)

    if target_lang is not None:
        st.session_state.target_lang = LANG_MAP[target_lang][0]

    # Only show translate button if a language is selected
    if st.session_state.target_lang:
        if st.button("Translate", type="primary"):
            try:
                translated_text = asyncio.run(
                    translate_text(st.session_state.transcription, st.session_state.detected_lang, st.session_state.target_lang)
                )
            except Exception as e:
                st.error(f"Error during translation: {e}")

            st.session_state.translated_text = translated_text

# Always display translated text if available
if st.session_state.translated_text:
    st.write("**TRANSLATED TEXT:**", st.session_state.translated_text)

    # Speak button stays available
    if st.button("Speak"):
        st.write('Generating Audio')
        filename = get_audio_filename(st.session_state.translated_text, st.session_state.target_lang)

        if not os.path.exists(filename):  # Check if file already exists
            tts = gTTS(text=st.session_state.translated_text, lang=st.session_state.target_lang)
            tts.save(filename)  

        st.audio(filename, format="audio/mp3")
        st.success('Audio generated Succesfully')
