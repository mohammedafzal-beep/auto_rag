import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.llms import CTransformers
from langchain.prompts import PromptTemplate
import os

def load_files(files):
    temp_dir = tempfile.mkdtemp()
    for uploaded_file in files:
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
    loader = DirectoryLoader(temp_dir, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(documents)

def initialize_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def initialize_pinecone(api_key, index_name, embeddings, text_chunks):
    os.environ["PINECONE_API_KEY"] = api_key
    return PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)

def initialize_llm():
    config = {'max_new_tokens': 512, 'temperature': 0.7}
    return CTransformers(model='TheBloke/Llama-2-7B-Chat-GGML', config=config)

def build_prompt():
    template = """
    Use the following pieces of information to answer the user's question.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    Context: {context}
    Question: {question}

    Only return the helpful answer below and nothing else.
    Helpful answer:
    """
    return PromptTemplate(template=template, input_variables=["context", "question"])
