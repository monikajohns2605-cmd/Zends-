from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "ZENDS offers mobile, broadband, cloud and IoT services",
    "Enterprise customers get SLA up to 99.9%",
    "Refund available within 7 days under conditions"
]

embeddings = model.encode(documents)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def retrieve_context(query):
    q_vec = model.encode([query])
    D, I = index.search(np.array(q_vec), k=1)
    return documents[I[0][0]]