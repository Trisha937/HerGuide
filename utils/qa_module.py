# # utils/qa_module.py
# import streamlit as st
# from utils.voice_utils import listen_to_voice, speak_text
# from transformers import pipeline
# from database import insert_question
# import pandas as pd


# qa_model = pipeline("question-answering", model="mrm8488/bert-multi-cased-finetuned-xquadv1")

# SCHEME_DETAILS = {
#     "प्रधानमंत्री जन धन योजना": {
#         "desc": "यह योजना गरीबों को बैंकिंग सेवाओं से जोड़ने के लिए बनाई गई है। इसमें मुफ्त बैंक खाता, डेबिट कार्ड और बीमा कवर मिलता है।",
#         "link": "https://pmjdy.gov.in"
#     },
#     "मुद्रा लोन योजना": {
#         "desc": "यह योजना छोटे कारोबारों को बिना गारंटी लोन देने के लिए है। इसमें शिशु, किशोर और तरुण श्रेणियाँ हैं।",
#         "link": "https://www.mudra.org.in"
#     },
#     "सुकन्या समृद्धि योजना": {
#         "desc": "बेटियों की शिक्षा और शादी के लिए बचत योजना। यह उच्च ब्याज दर और टैक्स में छूट देती है।",
#         "link": "https://www.nsiindia.gov.in"
#     },
#     "प्रधानमंत्री मातृ वंदना योजना": {
#         "desc": "यह योजना गर्भवती महिलाओं को पोषण और देखभाल के लिए आर्थिक सहायता प्रदान करती है।",
#         "link": "https://wcd.nic.in/schemes/pradhan-mantri-matru-vandana-yojana"
#     },
#     "राष्ट्रीय बालिका समृद्धि योजना": {
#         "desc": "यह योजना गरीब परिवारों की बालिकाओं को जन्म से लेकर शिक्षा तक आर्थिक सहायता देती है।",
#         "link": "https://wcd.nic.in/schemes/national-scheme-incentive-girl-child-secondary-education"
#     },
#     "प्रधानमंत्री उज्ज्वला योजना": {
#         "desc": "यह योजना गरीबी रेखा से नीचे रहने वाली महिलाओं को मुफ्त LPG गैस कनेक्शन देती है।",
#         "link": "https://www.pmuy.gov.in"
#     },
#     "एलआईसी जीवन बीमा": {
#         "desc": "जीवन बीमा के लिए भारत सरकार की भरोसेमंद योजना, जिससे परिवार को आर्थिक सुरक्षा मिलती है।",
#         "link": "https://licindia.in"
#     },
#     "एनपीएस योजना": {
#         "desc": "राष्ट्रीय पेंशन योजना जो रिटायरमेंट के बाद आर्थिक सुरक्षा देती है।",
#         "link": "https://enps.nsdl.com"
#     },
#     "आंगनवाड़ी लाभ योजना": {
#         "desc": "बच्चों, गर्भवती महिलाओं और धात्री माताओं को पोषण और स्वास्थ्य सेवाएं प्रदान करने वाली योजना।",
#         "link": "https://icds-wcd.nic.in"
#     },
#     "प्रधानमंत्री जीवन ज्योति बीमा योजना": {
#         "desc": "यह एक जीवन बीमा योजना है जिसमें वार्षिक प्रीमियम पर ₹2 लाख का बीमा कवर मिलता है।",
#         "link": "https://jansuraksha.gov.in/Files/PMJJBY/English/AboutPMJJBY.pdf"
#     },
#     "प्रधानमंत्री सुरक्षा बीमा योजना": {
#         "desc": "₹12 सालाना प्रीमियम पर ₹2 लाख का एक्सीडेंट बीमा।",
#         "link": "https://jansuraksha.gov.in/Files/PMSBY/English/AboutPMSBY.pdf"
#     },
#     "राष्ट्रीय स्वास्थ्य बीमा योजना": {
#         "desc": "गरीब परिवारों को अस्पताल में इलाज के लिए स्वास्थ्य बीमा सुविधा प्रदान करती है।",
#         "link": "https://www.india.gov.in/national-health-insurance-scheme"
#     }
# }


# def qa_interface():
#     st.subheader("🧠 वित्तीय प्रश्न पूछें")

#     if st.button("🎤 आवाज़ से पूछें"):
#         question = listen_to_voice()
#         st.write("आपका सवाल:", question)

#         context = "भारत सरकार कई वित्तीय योजनाएं चलाती है जैसे प्रधानमंत्री जन धन योजना, सुकन्या समृद्धि योजना, एलआईसी बीमा, एनपीएस योजना, मुद्रा लोन योजना आदि।"
#         response = qa_model(question=question, context=context)
#         answer = response['answer']

#         # Log to DB
#         insert_question(question, answer)

#         # Match with known schemes
#         matching_scheme = None
#         for scheme in SCHEME_DETAILS:
#             if scheme in answer:
#                 matching_scheme = scheme
#                 break

#         if matching_scheme:
#             details = SCHEME_DETAILS[matching_scheme]
#             full_answer = f"{answer}\n\n{details['desc']}\n\n📎 [योजना विवरण व पंजीकरण लिंक]({details['link']})"
#         else:
#             full_answer = answer

#         st.success(full_answer)
#         speak_text(full_answer)

import streamlit as st
from utils.voice_utils import listen_to_voice, speak_text
from transformers import pipeline
from database import insert_question
import pandas as pd

qa_model = pipeline("question-answering", model="mrm8488/bert-multi-cased-finetuned-xquadv1")

@st.cache_data
def load_schemes():
    df = pd.read_csv("her_schemes.csv", quotechar='"')
    return df

schemes_df = load_schemes()

def match_scheme_by_keywords(question, schemes_df):
    question_words = set(question.strip().lower().split())

    for _, row in schemes_df.iterrows():
        name_words = set(row['name'].strip().lower().split())
        desc_words = set(row['desc'].strip().lower().split())

        if question_words & name_words or question_words & desc_words:
            return row  # first match

    return None

def qa_interface():
    st.subheader("🧠 वित्तीय प्रश्न पूछें")

    if st.button("🎤 आवाज़ से पूछें"):
        question = listen_to_voice()
        st.write("आपका सवाल:", question)

        context = "भारत सरकार कई वित्तीय योजनाएं चलाती है जैसे प्रधानमंत्री जन धन योजना, सुकन्या समृद्धि योजना, एलआईसी बीमा, एनपीएस योजना, मुद्रा लोन योजना आदि।"
        response = qa_model(question=question, context=context)
        answer = response['answer']

        # Log to DB
        insert_question(question, answer)

        # Try to match answer with any scheme name
        matched_row = match_scheme_by_keywords(question, schemes_df)


        if matched_row is not None:
            full_answer = f"🔹 {matched_row['name']}\n\n📝 {matched_row['desc']}\n\n🔗 [योजना विवरण लिंक]({matched_row['link']})"
            speak_text(f"{matched_row['name']}। {matched_row['desc']}")
        else:
            full_answer = answer
            speak_text(answer)

        st.success(full_answer)
