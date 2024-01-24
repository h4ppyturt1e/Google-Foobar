import string
ALPHABETS = list(string.ascii_lowercase)
REVERSED_ALPHABETS = list(reversed(ALPHABETS))

A_DICT = {ALPHABETS[i]: REVERSED_ALPHABETS[i] for i in range(len(ALPHABETS))}

def solution(x):
    return ''.join([A_DICT[i] if i in A_DICT else i for i in x])