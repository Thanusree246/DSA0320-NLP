from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Corpus of documents
documents = [
    "The sky is blue.",
    "The sun is bright.",
    "The sun in the sky is bright.",
    "We can see the shining sun, the bright sun."
]

# Query
query = "bright sun"

# TF-IDF computation
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
query_vec = vectorizer.transform([query])

# Compute similarity
scores = cosine_similarity(query_vec, tfidf_matrix)

# Rank documents
ranked = scores.argsort()[0][::-1]
print("Ranked Documents:")
for rank in ranked:
    print(f"Document {rank+1}: {documents[rank]} (Score: {scores[0][rank]:.2f})")
