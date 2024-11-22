import spacy

nlp = spacy.load("en_core_web_sm")

sentence = "The quick brown fox jumps over the lazy dog."

doc = nlp(sentence)
for np in doc.noun_chunks:
    print(f"Noun Phrase: {np.text}")
