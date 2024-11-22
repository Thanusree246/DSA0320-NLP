
def check_agreement(grammar, start_symbol, tokens):
    def parse(symbol, tokens):
        if not tokens:
            return symbol == '', tokens

        if symbol not in grammar: 
            return tokens[0] == symbol, tokens[1:]

        for production in grammar[symbol]:
            remaining_tokens = tokens
            success = True
            for part in production.split():
                match, remaining_tokens = parse(part, remaining_tokens)
                if not match:
                    success = False
                    break
            if success:
                return True, remaining_tokens
        return False, tokens

    def check_subject_verb_agreement(tokens):
        singular_subjects = {"he", "she", "it", "dog", "cat"}
        plural_subjects = {"they", "dogs", "cats"}
        singular_verbs = {"eats", "likes"}
        plural_verbs = {"eat", "like"}

        subject = tokens[0]
        verb = tokens[1]

        if subject in singular_subjects and verb not in singular_verbs:
            return False
        if subject in plural_subjects and verb not in plural_verbs:
            return False
        return True

    success, remaining = parse(start_symbol, tokens)
    if success and not remaining:
        return check_subject_verb_agreement(tokens)
    return False

grammar = {
    'S': ['NP VP'],
    'NP': ['Pronoun', 'Det N'],
    'VP': ['V'],
    'Det': ['the'],
    'Pronoun': ['he', 'she', 'it', 'they'],
    'N': ['dog', 'dogs', 'cat', 'cats'],
    'V': ['eats', 'eat', 'likes', 'like']
}

sentence = "he eats"
tokens = sentence.split()
result = check_agreement(grammar, 'S', tokens)
print("Sentence has agreement:", result)
