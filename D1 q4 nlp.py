def generate_plural(noun):
    vowels = "aeiou"
    if noun.endswith('y') and noun[-2] not in vowels:
        return noun[:-1] + 'ies'
    elif noun.endswith(('s', 'sh', 'ch', 'x', 'z')):
        return noun + 'es'
    else:
        return noun + 's'


nouns = ["cat", "bus", "lady", "fox", "church"]
for noun in nouns:
    print(f"Plural of '{noun}': {generate_plural(noun)}")
