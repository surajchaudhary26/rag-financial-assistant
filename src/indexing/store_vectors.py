from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from src.ingestion.load_documents import load_pdfs_from_folder
from src.ingestion.split_text import split_documents
from src.utils.logger import setup_logger

logger = setup_logger()


def build_vector_store(data_path="data/raw", persist_dir="embeddings/vector_store"):
    """
    Create embeddings and store them in Chroma vector DB.
    """

    logger.info("Starting vector store build")

    # Load docs
    docs = load_pdfs_from_folder(data_path)

    # Split into chunks
    chunks = split_documents(docs)

    logger.info("Loading embedding model")

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    logger.info("Creating Chroma vector store")

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_dir,
    )

    vectordb.persist()

    logger.info(f"Vector store built and saved to {persist_dir}")
    logger.info(f"Total vectors stored: {len(chunks)}")

    return vectordb


if __name__ == "__main__":
    build_vector_store()
