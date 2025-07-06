import streamlit as st
from utils.voice_utils import speak_text

def recommend_interface(insert_yojana): ##
    st.subheader("📋 अपनी जानकारी भरें और योजनाएँ प्राप्त करें")

    with st.form("recommend_form"):
        name = st.text_input("नाम")
        age = st.number_input("उम्र", min_value=0)
        salary = st.number_input("सालाना आय (₹)")
        state = st.selectbox("राज्य", ["उत्तर प्रदेश", "महाराष्ट्र", "बिहार", "राजस्थान", "अन्य"])
        submit = st.form_submit_button("🎯 सुझाव प्राप्त करें")

    if submit:
        recommendation = f"{name} जी, आपकी जानकारी के अनुसार, आप {state} राज्य में रहने वाले हैं और आपकी उम्र {age} वर्ष है।"
        if salary < 200000:
            recommendation += " आप प्रधानमंत्री जन धन योजना, मुद्रा लोन योजना, और सुकन्या योजना (यदि applicable) के लिए पात्र हो सकते हैं।"
        else:
            recommendation += " आप एलआईसी बीमा और एनपीएस जैसी योजनाओं में निवेश कर सकते हैं।"
        insert_yojana(name, age, salary, state, recommendation) ##
        st.success(recommendation)
        speak_text(recommendation)
