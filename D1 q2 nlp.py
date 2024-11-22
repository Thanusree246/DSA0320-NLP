def fsa_match_ending_ab(string):
    state = 0 
    for char in string:
        if state == 0:
            state = 1 if char == 'a' else 0
        elif state == 1:
            state = 2 if char == 'b' else (1 if char == 'a' else 0)
    return state == 2  


test_strings = ["cab", "ab", "b", "abc", "abab"]
for string in test_strings:
    print(f"'{string}' ends with 'ab': {fsa_match_ending_ab(string)}")
