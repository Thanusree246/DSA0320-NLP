from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

text = "The sky is blue and the sun is shining."

tokenized_text = tokenizer([text], return_tensors="pt", padding=True)
translation = model.generate(**tokenized_text)

translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
print(f"Translation: {translated_text}")
