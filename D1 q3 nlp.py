import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


text = "The quick brown fox jumps over the lazy dog."

tokens = word_tokenize(text)

pos_tags = pos_tag(tokens)
print("Morphological Analysis (POS Tags):", pos_tags)
