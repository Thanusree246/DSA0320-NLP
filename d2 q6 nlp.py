import random
from collections import defaultdict
def generate_bigrams(text):
    words = text.split()
    bigrams = [(words[i], words[i+1]) for i in range(len(words) - 1)]
    return bigrams
def build_bigram_model(bigrams):
    model = defaultdict(list)
    for w1, w2 in bigrams:
        model[w1].append(w2)
    return model
def generate_text(model, start_word, length=10):
    text = [start_word]
    current_word = start_word
    
    for _ in range(length - 1):
        if current_word in model:
            next_word = random.choice(model[current_word])
            text.append(next_word)
            current_word = next_word
        else:
            break
    return ' '.join(text)
sample_text = "The quick brown fox jumps over the lazy dog. The lazy dog sleeps all day."
bigrams = generate_bigrams(sample_text)
bigram_model = build_bigram_model(bigrams)
start_word = "The"
generated_text = generate_text(bigram_model, start_word, length=15)
print("Generated Text:")
print(generated_text)
