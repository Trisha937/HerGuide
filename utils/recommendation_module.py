import streamlit as st
import pandas as pd
import os
from utils.voice_utils import speak_text

@st.cache_data
def load_schemes():
    csv_path = "her_schemes.csv"  # Make sure this file is in the project root
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    return pd.DataFrame(columns=["name", "desc", "link", "mediator_contacts"])

schemes_df = load_schemes()

def get_top_matching_schemes(user_text, salary):
    user_words = set(str(user_text).strip().lower().split())
    matches = []

    for _, row in schemes_df.iterrows():
        name_words = set(str(row["name"]).strip().lower().split())
        desc_words = set(str(row["desc"]).strip().lower().split())
        score = len(user_words & name_words) + len(user_words & desc_words)
        if score > 0:
            matches.append((score, row))

    if matches:
        sorted_matches = sorted(matches, key=lambda x: x[0], reverse=True)
        return [match[1] for match in sorted_matches[:3]]
    else:
        # Fallback if no relevant keywords found
        fallback = []
        if salary < 200000:
            keywords = ["जन धन", "मुद्रा", "सुकन्या", "उज्ज्वला", "समृद्धि", "बीमा"]
        else:
            keywords = ["एलआईसी", "एनपीएस", "विकास", "कौशल", "बीमा", "गुणवत्ता"]

        for _, row in schemes_df.iterrows():
            if any(keyword in str(row["name"]) for keyword in keywords):
                fallback.append(row)
        return fallback[:3]

def recommend_interface(insert_yojana, insert_feedback):
    st.subheader("📋 अपनी जानकारी भरें और योजनाएँ प्राप्त करें")

    with st.form("recommend_form"):
        name = st.text_input("नाम")
        age = st.number_input("उम्र", min_value=0)
        salary = st.number_input("सालाना आय (₹)")
        state = st.selectbox("राज्य", ["उत्तर प्रदेश", "महाराष्ट्र", "बिहार", "राजस्थान", "अन्य"])
        submit = st.form_submit_button("🎯 सुझाव प्राप्त करें")

    if submit:
        intro = f"{name} जी, आपकी जानकारी के अनुसार, आप {state} राज्य में रहने वाले हैं और आपकी उम्र {age} वर्ष है।"
        st.success(intro)
        speak_text(intro)

        user_query = f"{state} {salary}"
        top_matches = get_top_matching_schemes(user_query, salary)

        if top_matches:
            all_voice_text = ""
            for i, row in enumerate(top_matches, 1):
                scheme_name = row["name"]
                scheme_desc = row["desc"]
                scheme_link = row["link"]
                scheme_contact = row["mediator_contacts"]

                with st.container():
                    st.markdown(f"### {i}. 🔹 {scheme_name}")
                    st.markdown(f"**📝 विवरण:** {scheme_desc}")
                    st.markdown(f"**🔗 योजना लिंक:** [{scheme_link}]({scheme_link})")
                    st.markdown(f"**📞 संपर्क करें:** {scheme_contact}")
                    st.markdown("---")

                all_voice_text += f"{scheme_name}. {scheme_desc}. "

            speak_text(all_voice_text)

            # Save first recommendation summary to DB
            insert_yojana(name, age, salary, state, f"Suggested scheme: {top_matches[0]['name']}")

        else:
            msg = "क्षमा करें, कोई उपयुक्त योजना नहीं मिली।"
            st.warning(msg)
            speak_text(msg)

        # ✅ Feedback section
        feedback = st.radio("क्या यह सुझाव उपयोगी था?", ("हाँ", "नहीं"), index=None, horizontal=True)
        if feedback:
            insert_feedback("recommendation", f"{name} | {state} | ₹{salary}", feedback)
            st.info("धन्यवाद! आपकी प्रतिक्रिया सुरक्षित कर ली गई है।")
