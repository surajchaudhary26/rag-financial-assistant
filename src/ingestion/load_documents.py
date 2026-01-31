from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from src.utils.logger import setup_logger

logger = setup_logger()


def load_pdfs_from_folder(folder_path: str):
    """
    Load all PDFs from a folder using LangChain loader.
    """
    # Folder
    folder = Path(folder_path)

    if not folder.exists():
        logger.error(f"Folder not found: {folder_path}")
        return []
    # Scanning the Folder
    pdf_files = list(folder.glob("*.pdf"))

    if not pdf_files:
        logger.warning("No PDF files found in folder")
        return []

    all_docs = []
    
    # The Extraction Loop
    for pdf in pdf_files:
        logger.info(f"Loading PDF: {pdf.name}")

        loader = PyPDFLoader(str(pdf))
        docs = loader.load()

        logger.info(f"Loaded {len(docs)} pages from {pdf.name}")
        all_docs.extend(docs)

    logger.info(f"Total pages loaded: {len(all_docs)}")

    return all_docs


if __name__ == "__main__":
    docs = load_pdfs_from_folder("data/raw")

    print("\nSample page preview:\n")
    if docs:
        print(docs[0].page_content[:500])
