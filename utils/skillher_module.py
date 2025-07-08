# utils/skillher_module.py

import streamlit as st
import json
import os
from utils.voice_utils import speak_text
from database import fetch_profiles

# Load YouTube video links from JSON
def load_video_links():
    path = os.path.join("utils", "videos", "business_yt_links.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

video_data = load_video_links()

def skillher_interface(insert_profile, insert_feedback):
    st.subheader("💼 अपना व्यवसाय प्रोफ़ाइल जोड़ें")

    show_video = False
    selected_business = None

    with st.form("skillher_form"):
        name = st.text_input("आपका नाम")
        location = st.text_input("स्थान")
        business = st.selectbox("आप कौन सा काम करती हैं?", ["मेहंदी", "सिलाई", "ब्यूटी पार्लर", "कुकिंग", "अन्य"])
        contact = st.text_input("संपर्क जानकारी (फोन/ईमेल)")
        submit = st.form_submit_button("➕ जोड़ें")

    if submit:
        insert_profile(name, location, business, contact)
        success_msg = f"शुभकामनाएं {name} जी! आपका व्यवसाय ({business}) प्रोफ़ाइल जोड़ दिया गया है।"
        st.success(success_msg)
        speak_text(success_msg)
        show_video = True
        selected_business = business

    st.markdown("---")
    st.markdown("### 👩‍💼 हाल की व्यवसाय प्रोफ़ाइल:")

    profiles = fetch_profiles()
    if not profiles:
        st.info("कोई प्रोफ़ाइल अभी तक जोड़ी नहीं गई है।")
    else:
        for prof in profiles:
            name, location, business_p, contact = prof
            with st.container():
                st.markdown(f"**{name}** - {business_p}")
                st.markdown(f"📍 {location} | 📞 {contact}")
                st.markdown("---")

    # ✅ Show YouTube videos only after form submission
    if show_video and selected_business:
        st.markdown("### 📺 सुझावित YouTube वीडियो")
        if selected_business in video_data:
            for video in video_data[selected_business][:10]:
                st.markdown(f"👉 [{video['title']}]({video['url']})")
        else:
            st.info("इस व्यवसाय से संबंधित कोई वीडियो सुझाव उपलब्ध नहीं है।")

        # ✅ Feedback only after submission
        st.markdown("---")
        feedback = st.radio("क्या यह जानकारी उपयोगी थी?", ("हाँ", "नहीं"), index=None, horizontal=True)
        if feedback:
            insert_feedback("skillher", f"Skill area: {selected_business}", feedback)
            st.info("धन्यवाद! आपकी प्रतिक्रिया सुरक्षित कर ली गई है।")
