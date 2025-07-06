import streamlit as st
from utils.voice_utils import listen_to_voice, speak_text
from transformers import pipeline

# Load QA model
qa_model = pipeline("question-answering", model="mrm8488/bert-multi-cased-finetuned-xquadv1")

def qa_interface():
    st.subheader("🧠 वित्तीय प्रश्न पूछें")

    if st.button("🎤 आवाज़ से पूछें"):
        question = listen_to_voice()
        st.write("आपका सवाल:", question)

        context = """भारत सरकार कई वित्तीय योजनाएं चलाती है जैसे प्रधानमंत्री जन धन योजना, सुकन्या समृद्धि योजना,
        एलआईसी बीमा, एनपीएस योजना, मुद्रा लोन योजना आदि।"""

        response = qa_model(question=question, context=context)
        answer = response['answer']
        
        st.success("उत्तर: " + answer)
        speak_text(answer)

        st.markdown("👉 [योजनाओं के लिए रजिस्टर करें](https://www.india.gov.in/my-government/schemes)")

