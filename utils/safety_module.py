import streamlit as st
from utils.voice_utils import listen_to_voice, speak_text

SCAM_KEYWORDS = ["जल्दी", "पैसे", "OTP", "बैंक खाता", "लिंक", "धोखाधड़ी"]

def is_scam(text):
    return any(word in text for word in SCAM_KEYWORDS)

HELPLINES = {
    "महिला हेल्पलाइन": "1091",
    "राष्ट्रीय हेल्पलाइन": "181",
    "आपातकालीन": "112"
}

def safety_interface():
    st.subheader("🛡️ घोटाला पहचानें")

    if st.button("🎤 मेसेज बोलें"):
        message = listen_to_voice()
        st.write("आपका मेसेज:", message)

        if is_scam(message):
            warning = "⚠️ यह एक संभावित घोटाला है। कृपया सतर्क रहें और जानकारी किसी के साथ साझा न करें।"
        else:
            warning = "✅ यह संदेश सामान्य प्रतीत होता है।"

        st.warning(warning)
        speak_text(warning)

    st.subheader("📞 महिला हेल्पलाइन नंबर:")
    for name, number in HELPLINES.items():
        st.markdown(f"**{name}**: 📞 {number}")
