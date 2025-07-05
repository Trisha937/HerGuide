# app.py

import streamlit as st

def main():
    # ✅ TEMPORARY: Model status check (remove in production)
    from utils import init_gemini
    st.write("🧪 Model status:", "✅ Loaded" if init_gemini() else "❌ Not available")

    # ✅ Set app-wide config
    st.set_page_config(
        page_title="HerGuide",
        page_icon=":woman:",
        layout="centered"
    )

    # ✅ Initialize session state
    if "page" not in st.session_state:
        st.session_state.page = "welcome"

    # ✅ Welcome screen
    if st.session_state.page == "welcome":
        st.title("👋 Welcome to HerGuide")
        st.write("Empowering women with financial knowledge, micro-business opportunities and safety.")

        if st.button("Enter"):
            st.session_state.page = "home"
            st.rerun()

    # ✅ Home page with navigation links
    elif st.session_state.page == "home":
        st.title("🏠 Home")
        st.write("Choose a feature:")

        st.page_link("pages/QNA.py", label="🎙️ Voice Q&A")
        # st.page_link("pages/3_Recommendations.py", label="🏛️ Scheme Recommendations")
        # st.page_link("pages/4_SkillHER.py", label="🧵 SkillHER Micro-Business")
        # st.page_link("pages/5_Safety_Support.py", label="🛡️ Safety & Support")

if __name__ == "__main__":
    main()
