import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
import io
from datetime import datetime

# --- Configuration ---
@st.cache_resource
def init_gemini():
    try:
        genai.configure(
            api_key=st.secrets["GEMINI_API_KEY"],
            transport='rest'  # Ensures the correct endpoint
        )
        # Return model object
        return genai.GenerativeModel(
            'gemini-1.5-pro-latest',
            generation_config={"temperature": 0.7}
        )
    except Exception as e:
        st.error(f"🔴 Gemini Error: {str(e)}")
        return None

# --- Core Functions ---

import time

# Initialize the Gemini model once for use in ask_gpt
model = init_gemini()

def ask_gpt(prompt: str, lang: str = "hi") -> str:
    """Get Hindi response from Gemini with error handling and token/quota control."""
    if not model:
        return "System error: AI service unavailable"

    # Delay to avoid hitting request-per-minute quota
    time.sleep(2)  # Wait 2 seconds before making request

    try:
        response = model.generate_content(
            f"संक्षेप में उत्तर दें: '{prompt}'",  # shorter prompt = less tokens
            generation_config={
                "temperature": 0.6,
                "max_output_tokens": 60  # reduced from 150 to save quota
            }
        )

        return response.text.replace(".", "।")  # optional: Hindi sentence end

    except Exception as e:
        if "quota" in str(e).lower():
            st.toast("🚫 Quota exceeded. Please try again later.", icon="❌")
            return "कोटा समाप्त हो गया है, कृपया बाद में प्रयास करें।"
        st.toast(f"⚠️ Error: {str(e)}", icon="❌")
        return "क्षम करें, इस समय उत्तर देने में असमर्थ हूँ। कृपया बाद में प्रयास करें।"


def transcribe_audio(audio_bytes: bytes) -> str:
    """Convert Hindi audio to text with retry logic"""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(io.BytesIO(audio_bytes)) as source:
            audio = recognizer.record(source, duration=30)  # Limit to 30s
        return recognizer.recognize_google(audio, language="hi-IN")
    except sr.UnknownValueError:
        return "आवाज़ समझ नहीं आई। कृपया फिर से प्रयास करें।"
    except Exception as e:
        st.error(f"Transcription error: {str(e)}")
        return "तकनीकी समस्या हो रही है।"

def speak_text(text: str) -> bytes:
    """Convert Hindi text to natural-sounding speech"""
    try:
        tts = gTTS(
            text=text,
            lang="hi",
            slow=False,
            tld="co.in"  # Indian accent
        )
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp.read()
    except Exception as e:
        st.error(f"TTS failed: {str(e)}")
        return b""  # Return empty audio if failed
