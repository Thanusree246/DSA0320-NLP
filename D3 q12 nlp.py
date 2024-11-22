
def earley_parser(grammar, sentence):
    class State:
        def __init__(self, rule, dot, start, end):
            self.rule = rule
            self.dot = dot
            self.start = start
            self.end = end

        def is_complete(self):
            return self.dot == len(self.rule[1])

    def predict(state, chart, index):
        next_symbol = state.rule[1][state.dot]
        if next_symbol in grammar:
            for production in grammar[next_symbol]:
                chart[index].append(State((next_symbol, production), 0, index, index))

    def scan(state, chart, index, token):
        next_symbol = state.rule[1][state.dot]
        if next_symbol == token:
            chart[index + 1].append(State(state.rule, state.dot + 1, state.start, index + 1))

    def complete(state, chart, index):
        for prev_state in chart[state.start]:
            if not prev_state.is_complete() and prev_state.rule[1][prev_state.dot] == state.rule[0]:
                chart[index].append(State(prev_state.rule, prev_state.dot + 1, prev_state.start, index))

    words = sentence.split()
    chart = [[] for _ in range(len(words) + 1)]
    chart[0].append(State(('S', grammar['S'][0]), 0, 0, 0))

    for i in range(len(words) + 1):
        for state in chart[i]:
            if not state.is_complete():
                if state.dot < len(state.rule[1]) and state.rule[1][state.dot] in grammar:
                    predict(state, chart, i)
                elif i < len(words):
                    scan(state, chart, i, words[i])
            else:
                complete(state, chart, i)

    return any(state.rule[0] == 'S' and state.is_complete() and state.start == 0 and state.end == len(words) for state in chart[-1])

grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N'], ['Pronoun']],
    'VP': [['V', 'NP'], ['V']],
    'Det': [['a'], ['the']],
    'N': [['dog'], ['cat']],
    'Pronoun': [['I']],
    'V': [['see'], ['likes']]
}

sentence = "I see a dog"
result = earley_parser(grammar, sentence)
print("Sentence is valid:", result)
