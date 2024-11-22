import math

def pcfg_parser(grammar, start_symbol, tokens):
    def parse(symbol, tokens):
        if not tokens:
            return (math.log(1), symbol == '') if symbol == '' else (-math.inf, False)

        if symbol not in grammar: l
            if tokens[0] == symbol:
                return math.log(1), tokens[1:]
            return -math.inf, tokens

        best_prob = -math.inf
        best_remaining = tokens
        for production, prob in grammar[symbol]:
            remaining_tokens = tokens
            total_prob = math.log(prob)
            success = True
            for part in production.split():
                part_prob, remaining_tokens = parse(part, remaining_tokens)
                if part_prob == -math.inf:
                    success = False
                    break
                total_prob += part_prob
            if success and total_prob > best_prob:
                best_prob = total_prob
                best_remaining = remaining_tokens

        return best_prob, best_remaining

    prob, remaining = parse(start_symbol, tokens)
    return math.exp(prob) if not remaining else 0.0

grammar = {
    'S': [('NP VP', 0.9)],
    'NP': [('Det N', 0.8), ('Pronoun', 0.2)],
    'VP': [('V NP', 0.6), ('V', 0.4)],
    'Det': [('a', 0.5), ('the', 0.5)],
    'N': [('dog', 0.5), ('cat', 0.5)],
    'Pronoun': [('I', 1.0)],
    'V': [('see', 0.7), ('likes', 0.3)]
}

sentence = "I see a dog"
tokens = sentence.split()
probability = pcfg_parser(grammar, 'S', tokens)
print("Sentence probability:", probability)
