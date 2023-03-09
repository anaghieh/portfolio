import pandas as pd
import streamlit as st
import pandas as pd

st.header("The Best Company")

text1 = """
Learning a little each day adds up.
Research shows that students who are not khar are smart.
Set time aside to learn new things to prevent the likelihood of being a khare gav.
"""
st.text(text1)
st.subheader("Our Team")


col1, col2, col3 = st.columns([1, 1, 1])


df = pd.read_csv("data_test.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.text(row["role"])
        st.image("image_test/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.text(row["role"])
        st.image("image_test/" + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.text(row["role"])
        st.image("image_test/" + row["image"])
