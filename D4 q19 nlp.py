from nltk.corpus import wordnet as wn
from nltk.wsd import lesk


sentence = "The bank will not fail due to heavy rains."
word = "bank"

sense = lesk(sentence.split(), word)


if sense:
    print(f"Synset: {sense.name()}")
    print(f"Definition: {sense.definition()}")
    print(f"Examples: {sense.examples()}")
else:
    print("No suitable sense found.")
