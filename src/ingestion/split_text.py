from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.utils.logger import setup_logger
from src.ingestion.load_documents import load_pdfs_from_folder

logger = setup_logger()

def split_documents(docs, chunk_size=800, chunk_overlap=150):
    """
    Split documents into chunks using recursive splitter.
    """

    logger.info(
        f"Starting chunking | chunk_size={chunk_size}, overlap={chunk_overlap}"
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""],
    )

    chunks = splitter.split_documents(docs)

    logger.info(f"Total chunks created: {len(chunks)}")

    if chunks:
        avg_len = sum(len(c.page_content) for c in chunks) // len(chunks)
        logger.info(f"Average chunk length: {avg_len} chars")

    return chunks


if __name__ == "__main__":
    docs = load_pdfs_from_folder("data/raw")
    chunks = split_documents(docs)

    print("\nSample chunk preview:\n")
    if chunks:
        print(chunks[0].page_content[:500])