def build_prompt(context, query):
    context_text = "\n".join(context)

    prompt = f"""
You are a customer support assistant.
Answer the question using ONLY the information provided below.

Context:
{context_text}

Question:
{query}

Answer:
"""
    return prompt
