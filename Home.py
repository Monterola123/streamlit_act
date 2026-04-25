import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Roble M. Monterola Portfolio",
    page_icon="💻",
    layout="wide"
)

image = Image.open("assets/pic1.jpeg")

st.title("💻 My Portfolio")
st.write("Welcome to my simple portfolio created using Streamlit.")

st.divider()


st.header("About Me")

col1, col2 = st.columns([1,2])

with col1:
    st.image(image, use_container_width=True)

with col2:
    st.subheader("Martin R. Monterola 👋")
    st.write("""
Hello! I am **Martin R. Monterola**, a Computer Science student.

I enjoy learning programming and building simple applications.
I like practicing coding and learning new things.
             
🎓 School: DEBESMSCAT  
📚 Year Level: 3rd Year Student
""")

st.divider()

st.header("Skills")

st.write("Python")
st.progress(50)

st.write("HTML")
st.progress(60)

st.write("CSS")
st.progress(60)

st.divider()

st.header("Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("🎓 Student Record System")
    st.caption("Manages student data.")

with col2:
    st.write("🧮 Calculator App")
    st.caption("Performs basic calculations.")

with col3:
    st.write("🌐 Portfolio Website")
    st.caption("Displays my projects and skills.")

st.divider()


st.caption("© 2026 Martin Roble | Built with Streamlit")
