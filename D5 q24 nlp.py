from transformers import pipeline

classifier = pipeline("text-classification", model="mrm8488/t5-base-finetuned-dialogue-act")

dialog = [
    "Hi, how are you?",
    "I'm doing well, thanks! What about you?",
    "I'm good too. What do you want to do today?"
]

for utterance in dialog:
    result = classifier(utterance)[0]
    print(f"Utterance: {utterance}")
    print(f"Dialog Act: {result['label']}")
    print()
