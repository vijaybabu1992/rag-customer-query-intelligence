import numpy as np

def retrieve_documents(query, model, index, documents, top_k=2):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    return [documents[i] for i in indices[0]]
