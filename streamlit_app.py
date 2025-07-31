import streamlit as st
import tempfile
import os
from ingestion import ingest_files, process_documents, add_documents_to_vectorstore
from graph.graph import app  # Import the workflow app

st.set_page_config(page_title="Document Q&A App", layout="centered")
st.title("📄 Document Q&A with RAG")

st.write("""
Upload PDF, DOCX, CSV, or TXT files, ask a question, and get answers powered by your RAG system.
""")

uploaded_files = st.file_uploader(
    "Upload your documents (PDF, DOCX, CSV, TXT)",
    type=["pdf", "docx", "csv", "txt"],
    accept_multiple_files=True
)

question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if not question:
        st.warning("Please enter a question.")
    else:
        temp_paths = []
        if uploaded_files:
            for uploaded_file in uploaded_files:
                suffix = os.path.splitext(uploaded_file.name)[1]
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                    tmp.write(uploaded_file.read())
                    temp_paths.append(tmp.name)
        try:
            texts = ingest_files(temp_paths)
            splits = process_documents(texts)
            add_documents_to_vectorstore(splits)  # Add uploaded docs to vectorstore
            state = {
                "question": question,
                "web_search": False,
            }
            result = app.invoke(state)
            st.success("Result:")
            st.write(result)
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            for path in temp_paths:
                os.remove(path)

st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit and LangChain.")
