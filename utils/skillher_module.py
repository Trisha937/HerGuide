import streamlit as st

profiles = []

def skillher_interface(insert_profile):###
    st.subheader("💼 अपना व्यवसाय जोड़ें")

    with st.form("skill_form"):
        name = st.text_input("आपका नाम")
        location = st.text_input("स्थान")
        business = st.text_input("व्यवसाय प्रकार (जैसे मेहँदी, सिलाई)")
        contact = st.text_input("संपर्क जानकारी (फोन/ईमेल)")
        submit = st.form_submit_button("➕ जोड़ें")

    if submit:
        profiles.append({
            "name": name,
            "location": location,
            "business": business,
            "contact": contact
        })
        insert_profile(name, location, business, contact) ###
        st.success("प्रोफ़ाइल जोड़ी गई!")

    st.subheader("👩‍💼 उपलब्ध प्रोफ़ाइल:")
    for prof in profiles:
        with st.container():
            st.markdown(f"**{prof['name']}** - {prof['business']}")
            st.markdown(f"📍 {prof['location']} | 📞 {prof['contact']}")
            st.markdown("---")
