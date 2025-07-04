import streamlit as st
from audio_recorder_streamlit import audio_recorder
from utils import ask_gpt, transcribe_audio, speak_text


st.title("Voice-Based Q&A")
st.write("Ask your financial questions in Hindi.")

# Custom CSS to style the recorder
st.markdown("""
<style>
    .stAudioRecorder {
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Audio recorder with custom settings
audio_bytes = audio_recorder(
    text="🎤 Click to record",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="user",
    icon_size="2x",
    pause_threshold=10.0,  # Stop recording after 10 seconds of silence
)

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")  # Playback the recorded audio
    
    # Transcribe the audio
    with st.spinner("Processing your question..."):
        question = transcribe_audio(audio_bytes)
    
    if question and "sorry" not in question.lower():  # Check if transcription succeeded
        st.success("Transcription successful!")
        st.write("You asked:", question)
        
        # Get GPT response
        with st.spinner("Getting response from Saheli..."):
            response = ask_gpt(question, lang="hi")
        
        st.write("Saheli says:", response)
        
        # Convert response to speech
        with st.spinner("Generating audio response..."):
            response_audio = speak_text(response)
        st.audio(response_audio, format="audio/wav")
    else:
        st.error("Could not understand the audio. Please try again.")