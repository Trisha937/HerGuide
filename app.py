import streamlit as st

def main():
    # Temporary verification (remove after testing)
    from google.generativeai import get_model
    st.write("Model status:", get_model('gemini-1.5-pro-latest')) 
    
    st.set_page_config(page_title="HerGuide", page_icon=":woman:", layout="centered")
    if "page" not in st.session_state:
        st.session_state.page = "welcome"

    if st.session_state.page == "welcome":
        st.title("👋 Welcome to Saheli+SkillHER")
        st.write("Empowering women with financial knowledge and business opportunities.")
        if st.button("Enter"):
            st.session_state.page = "home"
            st.rerun()
    elif st.session_state.page == "home":
        st.title("🏠 Home")
        st.write("Choose a feature:")
        st.page_link("pages/QNA.py", label="🎙️ Voice Q&A")
        # st.page_link("pages/3_Recommendations.py", label="🏦 Scheme Recommendations")
        # st.page_link("pages/4_SkillHER.py", label="🧵 SkillHER Micro-Business")
        # st.page_link("pages/5_Safety_Support.py", label="🛡️ Safety & Support")

if __name__ == "__main__":
    main()