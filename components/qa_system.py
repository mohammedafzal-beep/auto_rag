import streamlit as st
from components.utils import initialize_llm, build_prompt
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA

def qa_system():
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Chat with Your Knowledge Base</h1>
            <p style="font-size:22px;">Ask questions based on the uploaded files.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "documents" not in st.session_state or "text_chunks" not in st.session_state:
        st.warning("No files uploaded. Please go back and upload files first.")
    else:
        docsearch = PineconeVectorStore.from_existing_index("medical-chatbot", st.session_state["embeddings"])
        prompt = build_prompt()
        llm = initialize_llm()
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=docsearch.as_retriever(search_kwargs={"k": 2}),
            chain_type_kwargs={"prompt": prompt},
        )

        # Custom CSS for styling the text_input box
        st.markdown(
            """
            <style>
            .stTextInput>div>input {
                height: 50px;
                font-size: 18px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        query = st.text_input("Ask a question:", label_visibility="collapsed", placeholder="Type your question here")
        if query:
            with st.spinner("Fetching answer..."):
                result = qa({"query": query})
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <p style='font-size:18px;'><strong>Response:</strong> {result['result']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
