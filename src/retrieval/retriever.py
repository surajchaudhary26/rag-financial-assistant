from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from src.utils.logger import setup_logger

logger = setup_logger()


def load_vector_store(persist_dir="embeddings/vector_store"):
    """
    Load existing persisted Chroma vector DB.
    """

    logger.info("Loading embedding model for retriever")

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    logger.info("Loading vector store from disk")

    vectordb = Chroma(
        persist_directory=persist_dir,
        embedding_function=embedding_model,
    )

    return vectordb


def search(query: str, k: int = 3):
    """
    Perform similarity search.
    """

    db = load_vector_store()

    logger.info(f"Running similarity search | query='{query}' | top_k={k}")

    results = db.similarity_search(query, k=k)

    logger.info(f"Retrieved {len(results)} chunks")

    return results


if __name__ == "__main__":
    q = "What is mutual funds?"

    docs = search(q, k=3)

    print("\nTop retrieved chunks:\n")

    for i, d in enumerate(docs, 1):
        print(f"\n--- Result {i} ---")
        print(d.page_content[:400])
        print("\nMetadata:", d.metadata)
