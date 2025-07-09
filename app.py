#app.py

import streamlit as st
from utils.qa_module import qa_interface
from utils.recommendation_module import recommend_interface
from utils.skillher_module import skillher_interface
from utils.safety_module import safety_interface

from databaseTest import (
    create_tables,
    insert_question,
    insert_yojana,
    insert_profile,
    insert_scam,
    insert_feedback  
)

# ✅ Initialize tables once when app loads
create_tables()

st.set_page_config(page_title="HerGuide", layout="wide")
st.title("🌸 HerGuide - नारी सुरक्षा एवं सशक्तिकरण एप")

# 📌 Tabs for different features
tab1, tab2, tab3, tab4 = st.tabs([
    "🧠 प्रश्न पूछें",
    "📋 योजना सुझाव",
    "💼 SkillHer",
    "🛡 सुरक्षा सहायता"
])

# 🔹 Q&A Tab with feedback collection
with tab1:
    qa_interface(insert_question, insert_feedback)

# 🔹 Recommendations Tab with feedback and bank links
with tab2:
    recommend_interface(insert_yojana, insert_feedback)

# 🔹 SkillHer Tab with profile card + YouTube business idea links
with tab3:
    skillher_interface(insert_profile, insert_feedback)

# 🔹 Safety Support Tab
with tab4:
    safety_interface()
