import streamlit as st
from utils.voice_utils import listen_to_voice, speak_text
from transformers import pipeline
import pandas as pd
import re


def qa_interface(insert_question, insert_feedback):
    st.subheader("🧠 वित्तीय प्रश्न पूछें")

    # Load HuggingFace QA model
    qa_model = pipeline("question-answering", model="mrm8488/bert-multi-cased-finetuned-xquadv1")

    @st.cache_data
    def load_schemes():
        return pd.read_csv("her_schemes.csv", quotechar='"')

    schemes_df = load_schemes()

    def clean_text(text):
        text = str(text).lower()
        text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
        return set(text.split())

    def match_schemes_by_overlap(question, df):
        q_words = clean_text(question)
        matches = []

        for _, row in df.iterrows():
            name_words = clean_text(row.get("name", ""))
            desc_words = clean_text(row.get("desc", ""))
            overlap = q_words & (name_words | desc_words)
            score = len(overlap)

            if score > 0:
                matches.append((score, row))

        # Return top 3 by descending score
        sorted_matches = sorted(matches, key=lambda x: x[0], reverse=True)
        return [m[1] for m in sorted_matches[:3]]

    if st.button("🎤 आवाज़ से पूछें"):
        question = listen_to_voice()
        st.write("आपका सवाल:", question)

        context = "भारत सरकार की वित्तीय योजनाओं में जन धन योजना, मुद्रा योजना, सुकन्या समृद्धि योजना, उज्ज्वला योजना आदि शामिल हैं।"
        response = qa_model(question=question, context=context)
        answer = response['answer']

        insert_question(question, answer)

        matched_rows = match_schemes_by_overlap(question, schemes_df)

        if matched_rows:
            all_voice_text = ""

            for i, row in enumerate(matched_rows, 1):
                scheme_name = row.get('name', '—')
                scheme_desc = row.get('desc', '—')
                scheme_link = row.get('link', '')
                scheme_contact = row.get('mediator_contacts', '')

                # Format clickable contacts
                contact_line = ""
                if scheme_contact:
                    contact_parts = [c.strip() for c in scheme_contact.split(",")]
                    clickable_contacts = []
                    for part in contact_parts:
                        if part.startswith("http") or "@" in part:
                            clickable_contacts.append(part)
                        elif part.replace("-", "").replace(" ", "").isdigit():
                            cleaned = ''.join(filter(str.isdigit, part))
                            clickable_contacts.append(f"[📞 {part}](tel:{cleaned})")
                        else:
                            clickable_contacts.append(part)
                    contact_line = " | ".join(clickable_contacts)

                with st.container():
                    st.markdown(f"### {i}. 🔹 {scheme_name}")
                    st.markdown(f"**📝 विवरण:** {scheme_desc}")
                    if scheme_link:
                        st.markdown(f"**🔗 योजना लिंक:** [{scheme_link}]({scheme_link})")
                    if contact_line:
                        st.markdown(f"**📞 संपर्क करें:** {contact_line}", unsafe_allow_html=True)
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
