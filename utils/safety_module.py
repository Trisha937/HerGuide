# utils/safety_module.py

import streamlit as st
from utils.voice_utils import listen_to_voice, speak_text
from database import insert_scam, insert_feedback

SCAM_KEYWORDS = ["जल्दी", "पैसे", "OTP", "बैंक खाता", "लिंक", "धोखाधड़ी", "मुनाफा", "लाभ"]
HELPLINES = {
    "महिला हेल्पलाइन": "1091",
    "राष्ट्रीय हेल्पलाइन": "181",
    "आपातकालीन": "112"
}

def is_scam(text):
    return any(word in text for word in SCAM_KEYWORDS)

def safety_interface():
    st.subheader("🛡️ घोटाला पहचानें")

    if st.button("🎤 मेसेज बोलें"):
        message = listen_to_voice()
        st.write("आपका मेसेज:", message)

        # Scam Detection Logic
        def get_scam_reason(text):
            matches = [word for word in SCAM_KEYWORDS if word in text]
            if matches:
                return f"Detect किया गया कीवर्ड: {', '.join(matches)}"
            return "कोई घोटाला संबंधित शब्द नहीं मिला"

        reason = get_scam_reason(message)

        if is_scam(message):
            warning = "⚠️ यह एक संभावित घोटाला है। कृपया सतर्क रहें।"
            insert_scam(message, flagged=True, reason=reason)
        else:
            warning = "✅ यह संदेश सामान्य प्रतीत होता है।"
            insert_scam(message, flagged=False, reason=reason)

        st.warning(warning)
        speak_text(warning)

        # ✅ Feedback Prompt
        st.markdown("___")
        feedback = st.radio("क्या यह जानकारी उपयोगी थी?", ("हाँ", "नहीं"), index=None, horizontal=True)
        if feedback:
            insert_feedback("safety", message, feedback)
            st.info("धन्यवाद! आपकी प्रतिक्रिया सुरक्षित कर ली गई है।")

    st.subheader("📞 महिला हेल्पलाइन नंबर:")
    for name, number in HELPLINES.items():
        st.markdown(f"📱 **{name}**: [📞 {number}](tel:{number})")
