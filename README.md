# 📊 RAG Financial Assistant

A Retrieval-Augmented Generation (RAG) based financial assistant that answers user queries strictly grounded in uploaded documents (PDFs).  
The system is designed with **hallucination control, safety, and modular architecture**, making it suitable for interviews, portfolios, and real-world financial use cases.

---

## 🚀 Key Features

- 📄 PDF document ingestion
- ✂️ Text chunking with overlap
- 🧠 Embedding generation using HuggingFace models
- 🗄️ Persistent vector storage using ChromaDB
- 🔍 Semantic retrieval (top-k similarity search)
- 🤖 LLM-based answer generation using **Gemini (free-tier friendly model)**
- 🛡️ Safety-aware responses (no financial advice, no hallucination)
- 🔄 Modular and provider-agnostic design
- 💬 CLI chat application
- 🧾 Structured logging

---

## 🧠 High-Level Architecture

User
↓
CLI Chat App
↓
RAG Pipeline
↓
Retriever (Vector DB)
↓
Relevant Context
↓
LLM (Gemini Flash Lite)
↓
Grounded Answer


---

## 📁 Project Structure

rag-financial-assistant/
│
├── src/
│ ├── ingestion/ # PDF loading
│ ├── indexing/ # Chunking, embeddings, vector store creation
│ ├── retrieval/ # Semantic retriever
│ ├── llm/ # LLM answer generation logic
│ ├── ragpipeline/ # RAG orchestration layer
│ ├── app/ # CLI chat application
│ ├── prompts/ # System prompt
│ └── utils/ # Logging utilities
│
├── embeddings/ # Persistent vector database files
├── requirements.txt
└── README.md


---

## ⚙️ Tech Stack

- **Python 3.13**
- **LangChain**
- **ChromaDB**
- **Sentence-Transformers**
- **Google Gemini API (free-tier model)**
- **Git & GitHub**

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/rag-financial-assistant.git
cd rag-financial-assistant
2️⃣ Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Set environment variables
export GOOGLE_API_KEY="your_gemini_api_key"
export PYTHONWARNINGS=ignore
📄 Document Ingestion & Indexing
Place PDF files in the ingestion directory and run:

python -m src.ingestion.load_documents
python -m src.indexing.build_vectorstore
This process:

loads documents

chunks text

generates embeddings

stores vectors persistently

▶️ Run the Chat Application
python -m src.app.chat
Example interaction:

💬 RAG Financial Assistant
You: What is a mutual fund?
Assistant: A mutual fund is an investment vehicle that pools money from investors...
Type exit or quit to stop.

🛡️ Safety & Ethics
The assistant does not give personalized financial advice

Responses are strictly based on retrieved document context

If information is missing, the model explicitly states so

Designed for compliance-sensitive financial environments

🧪 Example Behavior
User Query:

Suggest me mutual fund plan

Assistant Response:

I cannot suggest a specific mutual fund plan. However, the documents explain different types of schemes such as growth funds and income funds...

✔ Context-grounded
✔ No hallucination
✔ No advisory violation


This project demonstrates:

End-to-end RAG pipeline design

Semantic search using vector databases

Hallucination control using system prompts

Modular LLM integration (provider-agnostic)

Cost-aware model selection

Production-style logging and structure

📌 Future Enhancements
Source citations for answers

Web or API interface (FastAPI)

Query analytics and evaluation metrics

Improved retrieval tuning

👤 Author
Suraj Chaudhary
End-to-end RAG Financial Assistant built for learning, interviews, and real-world applications.