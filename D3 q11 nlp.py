def top_down_parser(grammar, start_symbol, tokens):
    def parse(symbol, tokens):
        if not tokens:
            return symbol == ''  

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

    success, remaining = parse(start_symbol, tokens)
    return success and not remaining

grammar = {
    'S': ['NP VP'],
    'NP': ['Det N', 'Pronoun'],
    'VP': ['V NP', 'V'],
    'Det': ['a', 'the'],
    'N': ['dog', 'cat'],
    'Pronoun': ['I'],
    'V': ['see', 'likes']
}


sentence = "I see a dog"
tokens = sentence.split()
result = top_down_parser(grammar, 'S', tokens)
print("Sentence is valid:", result)
