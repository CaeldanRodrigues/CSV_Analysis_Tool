from dotenv import load_dotenv
load_dotenv()
import streamlit as st

st.title("CSV Analysis Tool")
st.header("Please upload your CSV file here:")

data = st.file_uploader("Upload CSV file",type="csv")

query = st.text_area("Enter your query")
button = st.button("Generate Response")

if button:
    pass