import re

# Rule-based POS tagging function
def rule_based_pos_tagger(sentence):
    # Define rules: each pattern corresponds to a specific POS tag
    patterns = [
        (r'^\d+$', 'CD'),             # Cardinal numbers
        (r'(The|the|A|a|An|an)$', 'DT'),  # Determiners
        (r'.*ing$', 'VBG'),           # Gerunds (verbs ending in -ing)
        (r'.*ed$', 'VBD'),            # Past tense verbs
        (r'.*es$', 'VBZ'),            # Verbs ending in -es (3rd person singular present)
        (r'.*s$', 'NNS'),             # Plural nouns
        (r'.*ly$', 'RB'),             # Adverbs ending in -ly
        (r'.*', 'NN'),                # Default: Noun
    ]
    
    # Tokenize the sentence into words
    words = sentence.split()
    
    # Apply rules to each word
    tagged_words = []
    for word in words:
        for pattern, tag in patterns:
            if re.match(pattern, word):
                tagged_words.append((word, tag))
                break
    
    return tagged_words

# Test sentence
sentence = "The quick brown fox jumps over a lazy dog quickly"

# Perform POS tagging
tagged_sentence = rule_based_pos_tagger(sentence)

# Display the results
print("Sentence:", sentence)
print("Tagged Words:")
for word, tag in tagged_sentence:
    print(f"{word:10} : {tag}")
