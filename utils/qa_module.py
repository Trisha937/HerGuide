# utils/qa_module.py

import streamlit as st
from utils.voice_utils import listen_to_voice, speak_text
from transformers import pipeline
import pandas as pd

def qa_interface(insert_question, insert_feedback):
    st.subheader("🧠 वित्तीय प्रश्न पूछें")

    # Load HuggingFace QA model
    qa_model = pipeline("question-answering", model="mrm8488/bert-multi-cased-finetuned-xquadv1")

    @st.cache_data
    def load_schemes():
        return pd.read_csv("her_schemes.csv", quotechar='"')

    schemes_df = load_schemes()

    # Match schemes by overlapping keywords in name or description
    def match_scheme_by_keywords(question, schemes_df):
        question_words = set(question.strip().lower().split())
        matches = []

        for _, row in schemes_df.iterrows():
            name_words = set(str(row['name']).strip().lower().split())
            desc_words = set(str(row['desc']).strip().lower().split())

            name_score = len(question_words & name_words)
            desc_score = len(question_words & desc_words)
            total_score = name_score + desc_score

            if total_score > 0:
                matches.append((total_score, row))

        sorted_matches = sorted(matches, key=lambda x: x[0], reverse=True)
        return [match[1] for match in sorted_matches[:3]]

    if st.button("🎤 आवाज़ से पूछें"):
        question = listen_to_voice()
        st.write("आपका सवाल:", question)

        context = "भारत सरकार की वित्तीय योजनाओं में जन धन योजना, मुद्रा योजना, सुकन्या समृद्धि योजना, उज्ज्वला योजना आदि शामिल हैं।"
        response = qa_model(question=question, context=context)
        answer = response['answer']

        insert_question(question, answer)

        matched_rows = match_scheme_by_keywords(question, schemes_df)

        if matched_rows:
            all_voice_text = ""

            for i, row in enumerate(matched_rows, 1):
                scheme_name = row.get('name', '—')
                scheme_desc = row.get('desc', '—')
                scheme_link = row.get('link', '')
                scheme_contact = row.get('mediator_contacts', '')

                contact_line = f"\n\n{scheme_contact}" if scheme_contact else ""

                with st.container():
                    st.markdown(f"### {i}. 🔹 {scheme_name}")
                    st.markdown(f"**📝 विवरण:** {scheme_desc}")
                    st.markdown(f"**🔗 योजना लिंक:** [{scheme_link}]({scheme_link})")
                    st.markdown(f"**📞 संपर्क करें:** {contact_line}")
                    st.markdown("---")

                all_voice_text += f"{scheme_name}। {scheme_desc}. "

            speak_text(all_voice_text)
        else:
            st.warning("कोई उपयुक्त योजना नहीं मिली। कृपया पुनः प्रयास करें।")
            speak_text(answer)

        # Feedback prompt
        feedback = st.radio("क्या यह उत्तर उपयोगी था?", ("हाँ", "नहीं"), index=None, horizontal=True)
        if feedback:
            insert_feedback("qa", question, feedback)
            st.info("धन्यवाद! आपकी प्रतिक्रिया सुरक्षित कर ली गई है।")
