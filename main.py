import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Amir Naghieh")
    content = """
    Hi, I'm Amir. I'm a Data Engineer and on this page I seek to test my coding skills by writing various apps
    """
    st.info(content)

content2 = """
Welcome to my page! Below you can find my apps:
"""
st.text(content2)

