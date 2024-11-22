
class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []

def parse_tree(grammar, start_symbol, tokens):
    def parse(symbol, tokens):
        node = Node(symbol)
        if not tokens:
            return node if symbol == '' else None, tokens

        if symbol not in grammar:  
            if tokens[0] == symbol:
                return node, tokens[1:]
            return None, tokens

        for production in grammar[symbol]:
            remaining_tokens = tokens
            children = []
            for part in production.split():
                child, remaining_tokens = parse(part, remaining_tokens)
                if not child:
                    break
                children.append(child)
            else:
                node.children = children
                return node, remaining_tokens
        return None, tokens

    tree, remaining = parse(start_symbol, tokens)
    return tree if not remaining else None

def print_tree(node, indent=0):
    if node:
        print("  " * indent + node.symbol)
        for child in node.children:
            print_tree(child, indent + 1)


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
tree = parse_tree(grammar, 'S', tokens)

if tree:
    print("Parse Tree:")
    print_tree(tree)
else:
    print("Invalid sentence!")
