from collections import defaultdict
import random

# Step 1: Training data (small sample of sentences with tagged words)
# Format: [(word, POS), ...]
training_data = [
    [("The", "DT"), ("dog", "NN"), ("barks", "VBZ")],
    [("A", "DT"), ("cat", "NN"), ("meows", "VBZ")],
    [("The", "DT"), ("dog", "NN"), ("runs", "VBZ")],
    [("A", "DT"), ("bird", "NN"), ("flies", "VBZ")],
]

# Step 2: Build a stochastic model
def train_pos_tagger(data):
    # Dictionary to store {word: {tag: frequency}}
    word_tag_freq = defaultdict(lambda: defaultdict(int))

    # Populate frequency dictionary
    for sentence in data:
        for word, tag in sentence:
            word_tag_freq[word][tag] += 1

    # Convert frequencies to probabilities
    word_tag_prob = {}
    for word, tag_counts in word_tag_freq.items():
        total_count = sum(tag_counts.values())
        word_tag_prob[word] = {tag: count / total_count for tag, count in tag_counts.items()}

    return word_tag_prob

# Step 3: Use the model to predict POS tags
def stochastic_pos_tagger(model, sentence):
    pos_tags = []
    for word in sentence:
        if word in model:
            # Select the tag with the highest probability
            tag = max(model[word], key=model[word].get)
        else:
            # Assign a random tag for unknown words
            tag = random.choice(["NN", "VBZ", "DT"])
        pos_tags.append((word, tag))
    return pos_tags

# Train the model
pos_model = train_pos_tagger(training_data)

# Test sentence
test_sentence = ["The", "cat", "runs"]

# Predict POS tags
predicted_tags = stochastic_pos_tagger(pos_model, test_sentence)

# Display results
print("Sentence:", " ".join(test_sentence))
print("Predicted Tags:", predicted_tags)
