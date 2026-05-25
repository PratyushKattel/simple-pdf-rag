from ingestion.embedder import Embeder
from db import query_vector

embedder = Embeder()

def ask(question : str) -> list[str]:
    question_embedding = embedder.embed([question])
    results = query_vector(question_embedding[0])

    return results

if __name__ == "__main__":
    question = "What is the capital of France?"
    results = ask(question)
    print(results)  