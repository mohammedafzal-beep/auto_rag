import streamlit as st
from components.utils import load_files, split_text, initialize_embeddings, initialize_pinecone
import tempfile
import os

# Set up Pinecone API key
with open(r'C:\Users\afz31\AUTO_RAG\api_key.txt', "r") as file:
    PINECONE_API_KEY = file.read()

def file_upload():
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Upload Files for Knowledge Base</h1>
            <p style="font-size:22px;">Upload PDF or TXT files to build your custom knowledge base.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    files = st.file_uploader(
        "Drag and drop your files here or click to upload", 
        type=["pdf", "txt"], 
        accept_multiple_files=True, 
        label_visibility="collapsed"
    )

    if st.button("Process Files"):
        if files:
            with st.spinner("Processing files..."):
                documents = load_files(files)
                text_chunks = split_text(documents)
                embeddings = initialize_embeddings()
                initialize_pinecone(PINECONE_API_KEY, "medical-chatbot", embeddings, text_chunks)
            st.success("Files processed successfully!")
            st.session_state["documents"] = documents
            st.session_state["text_chunks"] = text_chunks
            st.session_state["embeddings"] = embeddings
        else:
            st.error("Please upload at least one file.")

