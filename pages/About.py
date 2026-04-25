import streamlit as st
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Martin Roble Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# ---------------- LOAD IMAGE ----------------
image = Image.open("assets/pic1.jpeg")

# ---------------- HEADER ----------------
st.title("👨‍💻 My Personal Portfolio")
st.write("Welcome to my simple portfolio created using Streamlit.")

st.divider()

col1, col2 = st.columns([1,2])

with col1:
    st.image(image, use_container_width=True)

with col2:
    st.subheader("Hi! I'm Martin R. Monterola 👋")

    st.write("""
I am a Computer Science student who enjoys learning programming 
and building simple applications.

I like learning how to code and create small projects.
""")

    if st.button("Say Hello"):
        st.success("Thanks for visiting my portfolio!")

st.divider()

st.subheader("Skills")

st.write("Python")
st.progress(90)

st.write("HTML")
st.progress(80)

st.write("CSS")
st.progress(75)

st.write("Streamlit")
st.progress(85)

st.divider()


st.subheader("Education")

st.write("""
College of Computing and Information Technology at
DEBESMSCAT

• Programming Fundamentals  
• Web Development  
• Software Design  
• Problem Solving
""")

st.divider()


st.subheader("My Favorite Skill")

skill = st.selectbox(
    "Choose a skill:",
    ["Python", "HTML", "CSS", "Streamlit"]
)

st.write(f"My selected skill is **{skill}**.")

st.divider()


