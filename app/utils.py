from deepgram import DeepgramClient, FileSource, PrerecordedOptions
from googletrans import Translator
import os
import hashlib
from dotenv import load_dotenv
import ast
import json

load_dotenv()
# Set Deepgram API key (Store securely in environment variables)
DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')

dg_client = DeepgramClient(DEEPGRAM_API_KEY)
file = open('app/lang_map.json')
LANG_MAP = json.load(file)


def map_lang(detected):
    for i in LANG_MAP:
        if detected in LANG_MAP[i]:
            return i
    return 'Unknown'

def transcribe_audio(audio_file):
     # Save uploaded file temporarily
        
    file_path = f"temp_{audio_file.name}"
    with open(file_path, "wb") as f:
        f.write(audio_file.getbuffer())

    # Send file to Deepgram for transcription
    with open(file_path, "rb") as f:
        buffer_data=f.read()

    payload: FileSource = {
        "buffer": buffer_data,
    }
    options = PrerecordedOptions(
        model="nova-2",
        smart_format=True,
        detect_language=True
    )
    # STEP 3: Call the transcribe_file method with the text payload and options
    response = dg_client.listen.rest.v("1").transcribe_file(payload, options)
    response_dict = ast.literal_eval(response.to_json(indent=4)) 

    # Remove temp file
    try:
        os.remove(file_path)
    except:
        pass

    # extract transcription from response
    transcription = response_dict['results']['channels'][0]['alternatives'][0]['transcript']
    detected_lang = response_dict['results']['channels'][0]['detected_language']
    norm_lang = map_lang(detected_lang)

    return transcription, detected_lang, norm_lang

async def translate_text(text, source_lang, target_lang):
    async with Translator() as translator:
        translation = await translator.translate(
            text,
            src = source_lang,
            dest = target_lang
        )
        translated_text = translation.text
    return translated_text


def get_audio_filename(text, lang):
    """Generate a unique filename for the TTS audio based on text content"""
    return f"audio_{hashlib.md5((text + lang).encode()).hexdigest()}.mp3"


