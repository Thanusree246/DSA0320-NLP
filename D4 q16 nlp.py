import spacy

nlp = spacy.load("en_core_web_sm")

text = "Tesla, founded by Elon Musk, is headquartered in Palo Alto, California."

doc = nlp(text)

for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}, Position: {ent.start_char}-{ent.end_char}")
