import streamlit as st
from components import (
    show_header, show_experience, show_projects,
    show_education, show_skills, show_certifications
)
from data_blessy import blessy_data

# --- Page Setup ---
st.set_page_config(
    page_title="Blessy Evangeline Aaron | Data Portfolio",
    page_icon="💜",
    layout="wide",
)

# --- Custom Background and Styling ---
# White card background for main content
card_style = """
<style>
section.main > div {
    background-color: #FFFFFF;
    border-radius: 18px;
    padding: 25px 40px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #F4EEFF 0%, #E3DFFD 100%);
}
[data-testid="stSidebar"] {
    background-color: #F8F5FF;
}
h1, h2, h3, h4 {
    color: #2D0A6B;
}
hr {
    border: 1px solid #9B59B6;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("Blessy Evangeline Aaron")
    st.markdown("[📄 Resume](./assets/blessy_resume.pdf)")
    st.markdown("📧 blessyaaron999@gmail.com")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/blessy-evangeline-30679b242)")
    st.markdown("[💻 GitHub](https://github.com/Blessy234)")

# --- Header ---
show_header(blessy_data)

# --- Tab Layout ---
tabs = st.tabs(["💼 Experience", "🚀 Projects", "🎓 Education", "🧠 Skills", "📜 Certifications"])

with tabs[0]:
    show_experience(blessy_data)

with tabs[1]:
    show_projects(blessy_data)

with tabs[2]:
    show_education(blessy_data)

with tabs[3]:
    show_skills(blessy_data)

with tabs[4]:
    show_certifications(blessy_data)
