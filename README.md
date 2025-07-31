# Corrective-RAG

Corrective RAG (Retrieval-Augmented Generation) is an advanced approach to RAG that **iteratively refines retrieved documents** to improve the final response quality. Instead of just retrieving documents and passing them to an LLM, Corrective RAG introduces **intermediate validation, filtering, and enhancement steps** to ensure only relevant and high-quality context is used.  

---

### **How Corrective RAG Works**

![image](https://github.com/user-attachments/assets/b387c119-d13d-4ac8-8532-91f05134d416)

1. **Retrieve Documents:**  
   - The system fetches documents from a database, vector store, or search engine.
  
2. **Grade Documents (Filtering & Scoring):**  
   - Each retrieved document is **evaluated** for relevance based on the query.
   - Irrelevant or low-quality documents are discarded.
  
3. **Decide Next Action:**  
   - If the retrieved documents are insufficient, the system can **refine the search, query external sources, or retrieve more documents**.
   - If the documents are relevant, it moves to generation.
  
4. **Web Search (Optional - External Augmentation):**  
   - If the retrieved documents are not enough, a web search or additional retrieval step is triggered.
  
5. **Generate Final Answer:**  
   - Only **high-quality, relevant** documents are passed to the LLM for response generation.

---

## 🚀 Getting Started

### Requirements
- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Install Dependencies
```bash
pip install -r requirements.txt
# Or manually:
pip install streamlit PyPDF2 python-docx pandas langchain chromadb python-dotenv
```

### Environment Variables
Create a `.env` file in the project root with your Google Gemini API key:
```
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## 🖥️ Usage

### 1. Run the Streamlit App
```bash
streamlit run streamlit_app.py
```

### 2. Upload Documents & Ask Questions
- Open the Streamlit web interface (usually at http://localhost:8501).
- Upload one or more documents (PDF, DOCX, CSV, or TXT).
- Enter your question in the text box.
- Click **Get Answer** to receive a response based on your documents.

### 3. Supported Document Types
- PDF (.pdf)
- Word (.docx)
- CSV (.csv)
- Plain Text (.txt)

---

## 🛠️ Project Structure
- `ingestion.py` — Handles document ingestion and processing for multiple file types.
- `streamlit_app.py` — User interface for uploading documents and querying.
- `graph/` — Core logic for retrieval, grading, and generation.
- `main.py` — Example script for backend usage.

---

## 🤖 How It Works (Quick Recap)
1. **Upload**: User uploads documents via the Streamlit app.
2. **Ingest**: The backend extracts and splits text from each document.
3. **Retrieve**: The system retrieves relevant chunks using vector search.
4. **Generate**: The LLM generates an answer using only the most relevant, high-quality context.

---

## 📢 Notes
- Make sure your API key is valid and you have internet access for web search features.
- For best results, upload clear, well-formatted documents.
- The system can be extended to support more file types or custom workflows.

---

## ❤️ Credits
Developed with Streamlit, LangChain, and Google Gemini.



