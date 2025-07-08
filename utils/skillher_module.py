import streamlit as st
import json
from utils.voice_utils import speak_text
import os
from database import fetch_profiles

# Load video links from JSON
def load_video_links():
    path = os.path.join("videos", "business_yt_links.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

video_data = load_video_links()

def skillher_interface(insert_profile):
    st.subheader("💼 अपना व्यवसाय प्रोफ़ाइल जोड़ें")

    with st.form("skillher_form"):
        name = st.text_input("आपका नाम")
        location = st.text_input("स्थान")
        business = st.selectbox("आप कौन सा काम करती हैं?", ["मेहंदी", "सिलाई", "ब्यूटी पार्लर", "कुकिंग", "अन्य"])
        contact = st.text_input("संपर्क जानकारी (फोन/ईमेल)")
        submit = st.form_submit_button("➕ जोड़ें")

    if submit:
        insert_profile(name, location, business, contact)
        success_msg = f"शुभकामनाएं {name} जी! आपका व्यवसाय ({business}) प्रोफ़ाइल जोड़ दिया गया है।"
        st.success(success_msg)
        speak_text(success_msg)

    st.markdown("---")
    st.markdown("### 👩‍💼 उपलब्ध प्रोफ़ाइल:")

    profiles = fetch_profiles()
    for prof in profiles:
        with st.container():
            st.markdown(f"**{prof[0]}** - {prof[2]}")  # name - business
            st.markdown(f"📍 {prof[1]} | 📞 {prof[3]}")  # location | contact
            st.markdown("---")

    st.markdown("### 📺 सुझावित YouTube वीडियो")

    if business in video_data:
        for video in video_data[business]:
            st.markdown(f"👉 [{video['title']}]({video['url']})")
    else:
        st.info("इस व्यवसाय से संबंधित कोई वीडियो सुझाव उपलब्ध नहीं है।")
