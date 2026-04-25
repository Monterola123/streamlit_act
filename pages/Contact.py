import streamlit as st

st.set_page_config(
    page_title="Contact Me",
    page_icon="📬",
    layout="wide"
)

st.title("📬 Get in Touch")
st.write("Feel free to send a message anytime.")

st.divider()


st.subheader("Contact Information")

st.write("""
📧 Email: monterolaroble@email.com  
💻 Role: Computer Science Student  
""")

st.divider()


st.subheader("Send a Message")

with st.form("contact_form"):

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submit = st.form_submit_button("Send")

    if submit:
        if name and email and message:
            st.success(f"Thank you {name}! Your message has been sent.")
        else:
            st.warning("Please fill in all fields.")

st.divider()

