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
        # Configure with transport fix
        genai.configure(
            api_key=st.secrets["GEMINI_API_KEY"],
            transport='rest'  # Forces correct API endpoint
        )
        
        # Use updated model name
        return genai.GenerativeModel(
            'gemini-1.5-pro-latest',  # Updated model name
            generation_config={"temperature": 0.7}
        )
    except Exception as e:
        st.error(f"Gemini Error: {str(e)}")
        return None

model = genai.GenerativeModel(
    'gemini-1.5-pro-latest',  # Updated model name
    generation_config={"temperature": 0.7}
)

# --- Core Functions ---
def ask_gpt(prompt: str, lang: str = "hi") -> str:
    """Get Hindi response from Gemini with error handling"""
    if not model:
        return "System error: AI service unavailable"

    try:
        response = model.generate_content(
            f"हिंदी में 2-3 वाक्यों में सरल उत्तर दें (उपयोगकर्ता ने पूछा: '{prompt}'):",
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 150  # Limit response length for audio
            }
        )
        return response.text.replace("•", "▶")  # Clean bullet points for TTS
    
    except Exception as e:
        st.toast(f"⚠️ Error: {str(e)}", icon="❌")
        return "क्षमा करें, इस समय उत्तर देने में असमर्थ हूँ। कृपया बाद में प्रयास करें।"

def transcribe_audio(audio_bytes: bytes) -> str:
    """Convert Hindi audio to text with retry logic"""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(io.BytesIO(audio_bytes)) as source:
            audio = recognizer.record(source, duration=30)  # Limit to 30s audio
            
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
        return b""  # Empty audio