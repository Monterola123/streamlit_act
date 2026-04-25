import streamlit as st

st.set_page_config(
    page_title="Work Portfolio",
    page_icon="🚀",
    layout="wide"
)


st.title("🚀 My Work Portfolio")
st.write("A simple showcase of my programming projects.")

st.divider()

projects = {
    "Student Record System": "Stores and manages student information.",
    "Calculator App": "Performs basic math operations.",
    "Personal Web Portfolio": "Shows my skills and projects."
}

st.subheader("Projects")

selected_project = st.selectbox(
    "Choose a project:",
    list(projects.keys())
)

st.info(projects[selected_project])

st.divider()


st.subheader("Portfolio Overview")

st.write("Completed Projects: 3")
st.write("Main Language: Python")
st.write("Tools: Streamlit")

st.divider()


st.subheader("Appreciation")

if st.button("Like this portfolio"):
    st.success("Thank you! ❤️ - Martin R. Monterola")

st.divider()
