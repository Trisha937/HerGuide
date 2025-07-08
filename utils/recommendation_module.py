import streamlit as st
import json
import os
from utils.voice_utils import speak_text

def load_bank_links():
    path = os.path.join("data", "banks_by_scheme.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

banks_data = load_bank_links()

def recommend_interface(insert_yojana, insert_feedback):
    st.subheader("📋 अपनी जानकारी भरें और योजनाएँ प्राप्त करें")

    with st.form("recommend_form"):
        name = st.text_input("नाम")
        age = st.number_input("उम्र", min_value=0)
        salary = st.number_input("सालाना आय (₹)")
        state = st.selectbox("राज्य", ["उत्तर प्रदेश", "महाराष्ट्र", "बिहार", "राजस्थान", "अन्य"])
        submit = st.form_submit_button("🎯 सुझाव प्राप्त करें")

    if submit:
        recommendation = f"{name} जी, आपकी जानकारी के अनुसार, आप {state} राज्य में रहने वाले हैं और आपकी उम्र {age} वर्ष है।"
        suggested_schemes = []
        
        if salary < 200000:
            suggested_schemes = ["प्रधानमंत्री जन धन योजना", "मुद्रा लोन योजना", "सुकन्या समृद्धि योजना"]
            recommendation += " आप प्रधानमंत्री जन धन योजना, मुद्रा लोन योजना, और सुकन्या योजना (यदि applicable) के लिए पात्र हो सकते हैं।"
        else:
            suggested_schemes = ["एलआईसी बीमा", "एनपीएस"]
            recommendation += " आप एलआईसी बीमा और एनपीएस जैसी योजनाओं में निवेश कर सकते हैं।"

        insert_yojana(name, age, salary, state, recommendation)
        st.success(recommendation)
        speak_text(recommendation)

        for scheme in suggested_schemes:
            st.markdown(f"---")
            st.markdown(f"### 📝 {scheme}")

            if scheme in banks_data:
                st.markdown("#### 🏦 इस योजना के लिए बैंक विकल्प:")
                for bank in banks_data[scheme]:
                    st.markdown(f"**{bank['bank']}**")
                    st.markdown(f"🔗 [Apply Here]({bank['apply_url']})")
                    st.markdown(f"📞 संपर्क करें: {bank['contact']}")
                    st.markdown("---")
            else:
                st.markdown("बैंक लिंक उपलब्ध नहीं हैं।")

        # Feedback prompt
        feedback = st.radio("क्या यह सुझाव उपयोगी था?", ("हाँ", "नहीं"), index=None, horizontal=True)
        if feedback:
            insert_feedback("recommendation", recommendation, feedback)
            st.info("धन्यवाद! आपकी प्रतिक्रिया सुरक्षित कर ली गई है।")
