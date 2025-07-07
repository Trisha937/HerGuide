# utils/qa_module.py

import streamlit as st
from utils.voice_utils import listen_to_voice, speak_text
from transformers import pipeline
from database import insert_question
import pandas as pd

# Load Hugging Face QA model
qa_model = pipeline("question-answering", model="mrm8488/bert-multi-cased-finetuned-xquadv1")

# Load scheme data
@st.cache_data
def load_schemes():
    df = pd.read_csv("her_schemes.csv", encoding="utf-8", quotechar='"')
    return df

schemes_df = load_schemes()

# Match question with any scheme name or desc
def match_scheme_by_keywords(question, schemes_df):
    question_words = set(question.lower().split())

    for _, row in schemes_df.iterrows():
        name = str(row['name']).lower()
        desc = str(row['desc']).lower()

        if any(word in name or word in desc for word in question_words):
            return row  # first matching row

    return None

def qa_interface():
    st.subheader("🧠 वित्तीय प्रश्न पूछें")

    if st.button("🎤 आवाज़ से पूछें"):
        question = listen_to_voice()
        st.write("आपका सवाल:", question)

        context = "भारत सरकार की वित्तीय योजनाएं जैसे जन धन, उज्ज्वला, सुकन्या, मुद्रा लोन, आदि हैं।"
        response = qa_model(question=question, context=context)
        answer = response['answer']

        insert_question(question, answer)
        matched_row = match_scheme_by_keywords(question, schemes_df)

        if matched_row is not None:
            scheme_name = matched_row.get("name", "—")
            scheme_desc = matched_row.get("desc", "—")
            scheme_link = matched_row.get("link", "")
            scheme_contact = matched_row.get("mediator_contacts", "")

            # Layout in columns
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 🏷 योजना नाम")
                st.write(scheme_name)

                st.markdown("#### 📝 योजना विवरण")
                st.write(scheme_desc)

            with col2:
                st.markdown("#### 🔗 आधिकारिक लिंक")
                if scheme_link:
                    st.markdown(f"[यहाँ क्लिक करें]({scheme_link})")
                else:
                    st.write("—")

                st.markdown("#### 📞 संपर्क जानकारी")
                if scheme_contact:
                    st.markdown(scheme_contact, unsafe_allow_html=True)
                else:
                    st.write("—")

            speak_text(f"{scheme_name}। {scheme_desc}")

        else:
            st.warning("कोई उपयुक्त योजना नहीं मिली।")
            speak_text(answer)
