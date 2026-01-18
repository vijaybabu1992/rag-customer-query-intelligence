# Retrieval-Augmented Generation (RAG) – Customer Query Intelligence

## 📌 Overview
This project demonstrates a **Retrieval-Augmented Generation (RAG)** architecture designed to answer customer queries by grounding responses in domain-specific documents.

The goal is to reduce hallucination in language-model-based systems by retrieving relevant context from a trusted knowledge base before generating responses.

This is a **personal applied GenAI project** created for learning and demonstration purposes.

---

## 🧠 Business Context
In regulated domains such as banking and financial services, customer-facing teams rely on large volumes of unstructured documents:
- Policy manuals
- FAQs
- Support guides

Traditional LLMs can generate fluent answers but may hallucinate or provide outdated information.  
RAG mitigates this risk by **augmenting generation with retrieved, verified context**.

---

## 🏗️ Architecture Overview

User Query
↓
Query Embedding
↓
Vector Similarity Search (FAISS)
↓
Relevant Document Retrieval
↓
Prompt Construction with Context
↓
LLM Response (Simulated)


---

## ⚙️ Technical Approach

### 1. Document Ingestion
- Synthetic policy documents are stored as plain text.
- Documents are split into logical chunks for embedding.

### 2. Embeddings
- Sentence embeddings are generated using `sentence-transformers`.
- These embeddings represent semantic meaning of documents.

### 3. Vector Store
- FAISS is used to store embeddings and perform similarity search.
- Top-K relevant documents are retrieved for each query.

### 4. Prompt Construction
- Retrieved context is injected into a structured prompt.
- The prompt explicitly instructs the model to use **only provided context**.

### 5. Response Generation
- The LLM layer is **simulated** to demonstrate end-to-end RAG flow.
- This keeps the architecture LLM-agnostic and provider-independent.

---

## 🧪 Example Query

When do credit card rewards expire?

**Retrieved Context:**
Policy B: Credit card rewards expire after 24 months from the date of accrual.

**Answer (Simulated):**
Credit card rewards expire after 24 months from the date of accrual.


---

## 🛠️ Tech Stack
- Python
- SentenceTransformers
- FAISS (Vector Search)
- NumPy

---

## ⚠️ Important Note on LLM Usage
Due to the absence of paid LLM API access, the response generation layer is intentionally simulated.

However, this project **fully implements the core RAG components**:
- Document chunking
- Embedding generation
- Vector-based retrieval
- Prompt construction with grounded context

The architecture is **LLM-agnostic** and can be easily extended to OpenAI, Anthropic, Gemini, or open-source models.

---

## 🔒 Disclaimer
This project uses **synthetic and publicly safe data only**.  
No proprietary, confidential, or company-specific data was used.

---

## 🚀 Future Enhancements
- Integrate open-source LLMs (e.g., FLAN-T5, LLaMA)
- Add evaluation metrics for retrieval quality
- Build a simple Streamlit UI
- Add citation-based answers

---

## 👤 Author
**Vijay Babu Kommuri**  
Data Scientist | Applied ML & GenAI  
