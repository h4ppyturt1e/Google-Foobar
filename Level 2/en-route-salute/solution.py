def solution(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '>':
            count += s[i:].count('<')
        elif s[i] == '<':
            count += s[:i].count('>')
    return count

tests = [("<<>><", 4), (">----<", 2)]

for test in tests:
    print(f"{solution(test[0]) == test[1]}: {solution(test[0])} == {test[1]}")