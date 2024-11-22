from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "ran", "runner", "easily", "fairness"]

stemmed_words = [stemmer.stem(word) for word in words]
print("Original words:", words)
print("Stemmed words:", stemmed_words)
