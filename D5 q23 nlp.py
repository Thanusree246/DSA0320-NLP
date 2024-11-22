from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

text = "The sky is blue. Birds are flying. It is a sunny day."

sentences = text.split(". ")
embeddings = model.encode(sentences)
similarities = [
    cosine_similarity([embeddings[i]], [embeddings[i + 1]])[0][0]
    for i in range(len(embeddings) - 1)
]

coherence_score = sum(similarities) / len(similarities)
print(f"Coherence Score: {coherence_score:.2f}")
