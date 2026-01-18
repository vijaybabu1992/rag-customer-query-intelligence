from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def create_vector_store(documents):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(documents)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    return index, model
