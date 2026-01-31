# RAG Financial Assistant

A Retrieval-Augmented Generation (RAG) based financial assistant that answers user queries strictly from provided financial documents (PDFs). The system is designed to avoid hallucinations, follow safety constraints, and demonstrate real-world LLM engineering practices suitable for interviews and production-style projects.

## Overview

This project implements an end-to-end RAG pipeline that ingests financial documents, stores semantic embeddings in a vector database, retrieves relevant context for a user query, and uses a large language model to generate grounded and safe answers. The assistant focuses on educational responses and avoids providing personalized financial advice.

## Features

- PDF document ingestion  
- Text chunking with overlap  
- Embeddings using HuggingFace sentence-transformers  
- Persistent vector storage using ChromaDB  
- Semantic similarity search (retriever)  
- LLM-based answer generation using Gemini (free-tier friendly model)  
- Safety-aware responses (no hallucination, no financial advice)  
- Modular project architecture  
- CLI-based chat application  
- Structured logging  

## Architecture

User Query → CLI Chat App → RAG Pipeline → Retriever (Vector DB) → Relevant Context → LLM (Gemini Flash Lite) → Grounded Answer

## Project Structure

rag-financial-assistant/
├── src/
│   ├── ingestion/          # PDF loading
│   ├── indexing/           # Chunking, embeddings, vector store creation
│   ├── retrieval/          # Semantic retriever
│   ├── llm/                # LLM answer generation
│   ├── ragpipeline/        # RAG orchestration logic
│   ├── app/                # CLI chat application
│   ├── prompts/            # System prompt
│   └── utils/              # Logging utilities
├── embeddings/             # Persistent vector database
├── requirements.txt
└── README.md

## Tech Stack

- Python 3.13  
- LangChain  
- ChromaDB  
- Sentence-Transformers  
- Google Gemini API (free-tier model)  
- Git & GitHub  

## Setup

Clone the repository:

git clone https://github.com/surajchaudhary26/rag-financial-assistant.git
cd rag-financial-assistant

Create and activate a virtual environment:

python -m venv .venv  
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Set environment variables:

export GOOGLE_API_KEY="your_gemini_api_key"  
export PYTHONWARNINGS=ignore

## Document Ingestion and Indexing

Place PDF files in the ingestion directory and run:

python -m src.ingestion.load_documents  
python -m src.indexing.build_vectorstore

This loads documents, creates chunks, generates embeddings, and stores them in the vector database.

## Run the Chat Application

python -m src.app.chat

Example:

You: What is a mutual fund?  
Assistant: A mutual fund is an investment vehicle that pools money from multiple investors...

Type `exit` or `quit` to stop the chat.

## Safety and Ethics

- The assistant does not provide personalized financial advice  
- All answers are grounded in retrieved document context  
- If information is missing, the system explicitly states so  
- Designed for compliance-sensitive financial use cases  

## Example Behavior

Query:  
Suggest me a mutual fund plan

Response:  
I cannot suggest a specific mutual fund plan. However, the documents explain different types of schemes such as growth funds and income funds.

This demonstrates safe, context-based, non-hallucinated behavior.

## Interview Highlights

- End-to-end RAG pipeline implementation  
- Semantic search using vector databases  
- Hallucination control via system prompts  
- Modular and provider-agnostic LLM design  
- Cost-aware model selection  
- Production-style logging and structure  

## Author

Suraj Chaudhary  
RAG Financial Assistant built for interviews, learning, and real-world experimentation.
