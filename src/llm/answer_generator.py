from google import genai
from google.genai import types
from pathlib import Path
import os

from src.retrieval.retriever import search
from src.utils.logger import setup_logger

logger = setup_logger()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def load_system_prompt():
    return Path("src/prompts/system_prompt.txt").read_text()


def build_context(docs):
    return "\n\n".join(d.page_content for d in docs)


def answer_query(query: str):
    logger.info(f"Answering query: {query}")

    system_prompt = load_system_prompt()

    docs = search(query, k=4)

    if not docs:
        return "No relevant documents found."

    context = build_context(docs)

    logger.info(f"Context length chars: {len(context)}")

    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=f"Context:\n{context}\n\nQuestion: {query}",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        )
    )

    return response.text


if __name__ == "__main__":
    q = "What is expense ratio in mutual funds?"

    ans = answer_query(q)

    print("\nFINAL ANSWER:\n")
    print(ans)
