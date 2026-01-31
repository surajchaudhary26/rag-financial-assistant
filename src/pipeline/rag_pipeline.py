from src.llm.answer_generator import answer_query
from src.utils.logger import setup_logger

logger = setup_logger()


class RAGPipeline:
    def __init__(self):
        logger.info("RAGPipeline initialized")

    def run(self, query: str) -> str:
        logger.info(f"Running RAG pipeline for query: {query}")

        answer = answer_query(query)

        logger.info("RAG pipeline finished")

        return answer
