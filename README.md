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



