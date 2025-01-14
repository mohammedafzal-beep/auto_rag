import streamlit as st
from components.file_upload import file_upload
from components.qa_system import qa_system

# Streamlit App Config
st.set_page_config(page_title="RAG Chatbot", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Upload Files", "Chat"])

if page == "Upload Files":
    file_upload()

if page == "Chat":
    qa_system()
