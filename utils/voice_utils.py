import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import streamlit as st

def listen_to_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 कृपया बोलें...")
        audio = recognizer.listen(source, timeout=5)
    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        return text
    except sr.UnknownValueError:
        return "क्षमा करें, मैं समझ नहीं पाई।"
    except Exception as e:
        return str(e)

def speak_text(text):
    tts = gTTS(text=text, lang='hi')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format="audio/mp3")
