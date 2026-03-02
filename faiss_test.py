import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
texts = [
    "Python is great for data science",
    "I love writing backend APIs",
    "Cooking pasta is fun"
]
embeddings = model.encode(texts)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))
query = "I enjoy Python programming"
query_embedding = model.encode([query])
distances, indices = index.search(query_embedding, k=2)
for idx in indices[0]:
    print(texts[idx])
