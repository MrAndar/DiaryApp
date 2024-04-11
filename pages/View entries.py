import streamlit as st
import glob

# Streamlit widgets
st.title("Past entries")

filepaths = glob.glob("entries/*.txt")
for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()
        title = str(filepath).split("-")[-1].split(".")[0][1:]
        date = str(filepath)[8:26]

        st.subheader(title)
        st.write(date)
        st.write(content)
