from vector_store import create_vector_store
from retriever import retrieve_documents
from prompt_builder import build_prompt

def load_documents(file_path):
    with open(file_path, "r") as f:
        return f.read().split("\n\n")

if __name__ == "__main__":
    documents = load_documents("data/policies.txt")

    index, model = create_vector_store(documents)

    user_query = "When do credit card rewards expire?"
    retrieved_docs = retrieve_documents(
        user_query, model, index, documents
    )

    prompt = build_prompt(retrieved_docs, user_query)

    print("----- PROMPT SENT TO LLM -----")
    print(prompt)

    print("----- SIMULATED ANSWER -----")
    print("Credit card rewards expire after 24 months from the date of accrual.")
