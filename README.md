# RAG Chatbot 🤖

A **Streamlit**-based application that uses Retrieval-Augmented Generation (RAG) to build an intelligent chatbot capable of answering questions based on uploaded documents.

---

## Features 🔄

- **File Upload** 📂: Upload documents to create a knowledge base for the chatbot.
- **Chat Interface** 🤖: Interact with the chatbot to retrieve answers from the uploaded documents.
- **Modular Design** 🔄: Easily extendable with components for different functionalities.

---

## Installation 🚀

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/auto_rag.git
   cd auto_rag
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## File Structure 📚

```
auto_rag-main/
├── app.py                # Main application file
├── components/           # Modular components for the app
│   ├── file_upload.py    # Handles file uploads
│   ├── qa_system.py      # Implements the chatbot
│   └── utils.py          # Utility functions
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Dependencies 💪

- `streamlit` - Web framework for building the UI
- `langchain` - Framework for building LLM applications
- `langchain_pinecone` - Integration with Pinecone for vector storage
- `pypdf` - PDF file processing
- `sentence-transformers` - Pretrained models for text embeddings
- `ctransformers` - Model-specific utilities

Install all dependencies using the `requirements.txt` file.

---

## How to Use 🔄

1. **Upload Files** 📂: Go to the "Upload Files" section to add documents.
2. **Ask Questions** 🕵️‍♂️: Switch to the "Chat" section and interact with the chatbot.
3. **Get Answers** 🎮: Receive responses based on the uploaded content.

---

## Contribution Guidelines 📚

We welcome contributions! To get started:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License 🌐

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements 💕

- Inspired by modern RAG techniques and Streamlit-based applications.
- Thanks to the open-source community for the amazing tools!

---

Start building intelligent applications with RAG today! 🚀

