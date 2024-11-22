def parse_fopc(expression):
    components = {}
    if "∀" in expression or "∃" in expression:
        components['Quantifier'], rest = expression.split(" ", 1)
    else:
        rest = expression
    predicate, args = rest.split("(")
    args = args.strip(")").split(",")
    components['Predicate'] = predicate
    components['Arguments'] = args
    return components

expression = "∀x Human(x) → Mortal(x)"
parsed = parse_fopc(expression)
print(parsed)
