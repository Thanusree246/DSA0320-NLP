import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input text
text = "Natural Language Processing enables computers to understand human language."

# Step 1: Tokenize the text into words
tokens = word_tokenize(text)

# Step 2: Perform POS tagging
pos_tags = pos_tag(tokens)

# Display the results
print("Word  : POS Tag")
print("----------------")
for word, tag in pos_tags:
    print(f"{word:6}: {tag}")
