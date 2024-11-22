import spacy
import neuralcoref

nlp = spacy.load("en_core_web_sm")

neuralcoref.add_to_pipe(nlp)

text = "Alice loves her cat. She takes it to the park every day."

doc = nlp(text)

if doc._.has_coref:
    print("Resolved Text:", doc._.coref_resolved)
else:
    print("No references found.")
