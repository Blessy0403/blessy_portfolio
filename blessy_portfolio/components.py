import streamlit as st
import os

# --------------------------
# Helper: Aesthetic divider
# --------------------------
def color_divider(color="#9B59B6"):
    st.markdown(
        f"<hr style='border:2px solid {color}; border-radius:10px;'>",
        unsafe_allow_html=True
    )


# --------------------------
# Header Section
# --------------------------
def show_header(data):
    col1, col2 = st.columns([1, 3])
    with col1:
        if os.path.exists(data["profile_img"]):
            st.image(data["profile_img"], width=220)
    with col2:
        st.markdown(
            f"""
            <h1 style='color:#2D0A6B;margin-bottom:0;'>{data['name']}</h1>
            <h3 style='color:#6A1B9A;margin-top:0;'>{data['title']}</h3>
            <p style='font-size:16px;'>{data['about']}</p>
            """,
            unsafe_allow_html=True
        )
        st.markdown(f"[📄 View Resume]({data['resume_link']})")
        st.markdown(
            f"📧 [Email]({data['contact']['email']}) | 🔗 [LinkedIn]({data['contact']['linkedin']}) | 💻 [GitHub]({data['contact']['github']})"
        )
    color_divider()


# --------------------------
# Experience
# --------------------------
def show_experience(data):
    st.markdown("### 💼 Experience")
    for exp in data["experience"]:
        st.subheader(f"{exp['role']} – {exp['company']}")
        st.caption(exp["duration"])
        for d in exp["details"]:
            st.markdown(f"- {d}")
    color_divider()


# --------------------------
# Projects
# --------------------------
def show_projects(data):
    st.markdown("### 🚀 Projects")
    for proj in data["projects"]:
        st.markdown(
            f"""
            <div style="background-color:#FFFFFF;border-radius:12px;padding:15px 20px;margin-bottom:12px;
            box-shadow:0 2px 6px rgba(0,0,0,0.1);">
                <h4 style="color:#2D0A6B;">{proj['title']}</h4>
                <p style="font-size:15px;">{proj['description']}</p>
                <p style="color:#6A1B9A;font-style:italic;">🛠 Tools: {', '.join(proj['tools'])}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    color_divider()


# --------------------------
# Education (Card Layout)
# --------------------------
def show_education(data):
    st.markdown("### 🎓 Education")
    for edu in data["education"]:
        st.markdown(
            f"""
            <div style="background:linear-gradient(90deg,#E9D5FF,#F3E8FF);
            border-radius:12px;padding:15px 25px;margin-bottom:10px;">
                <h4 style="color:#4A148C;margin-bottom:4px;">{edu['degree']}</h4>
                <p style="margin:0;"><strong>{edu['institution']}</strong></p>
                <p style="color:#555;">{edu['duration']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    color_divider()


# --------------------------
# Skills (Badge Layout)
# --------------------------
def show_skills(data):
    st.markdown("### 🧠 Technical Skills")
    skills_html = " ".join(
        [
            f"<span style='background-color:#D6BCFA;color:#2D0A6B;padding:8px 14px;"
            f"margin:5px;display:inline-block;border-radius:25px;font-size:14px;font-weight:500;'>💡 {skill}</span>"
            for skill in data["skills"]
        ]
    )
    st.markdown(
        f"<div style='margin-top:10px;'>{skills_html}</div>",
        unsafe_allow_html=True,
    )
    color_divider()


# --------------------------
# Certifications (Ribbon Style)
# --------------------------
def show_certifications(data):
    st.markdown("### 📜 Certifications")
    for cert in data["certifications"]:
        st.markdown(
            f"""
            <div style="background-color:#F8F5FF;border-left:5px solid #9B59B6;
            padding:10px 18px;border-radius:8px;margin-bottom:10px;">
                <p style="margin:0;font-weight:500;color:#4A148C;">🏅 {cert}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    color_divider()
