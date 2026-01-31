import sys
import warnings

from src.pipeline.rag_pipeline import RAGPipeline
from src.utils.logger import setup_logger
from langchain_core._api.deprecation import LangChainDeprecationWarning

# Silence noisy warnings for clean chat experience
warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

logger = setup_logger()


def main():
    logger.info("Starting RAG Chat Application")

    rag = RAGPipeline()

    print("\n💬 RAG Financial Assistant")
    print("Type your question below.")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            query = input("You: ").strip()

            if query.lower() in {"exit", "quit"}:
                print("\n👋 Exiting chat. Goodbye!")
                break

            if not query:
                continue

            answer = rag.run(query)

            print("\nAssistant:")
            print(answer)
            print("-" * 60)

        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted. Goodbye!")
            sys.exit(0)

        except Exception as e:
            logger.exception("Error during chat execution")
            print("⚠️ Something went wrong. Please try again.\n")


if __name__ == "__main__":
    main()
