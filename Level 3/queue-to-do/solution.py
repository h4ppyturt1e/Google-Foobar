
from functools import reduce


def solution(start, length):
    if length == 0:
        return 0
    
    toBeXORed = []
    original_length = length
    cur = start
    missed = 0
    while missed != original_length:
        for _ in range(length):
            toBeXORed.append(cur)
            cur += 1
        
        for _ in range(missed):
            cur += 1

        length -= 1
        missed += 1
    
    # XOR all the numbers in the list
    print(toBeXORed)
    res = reduce(lambda x, y: x ^ y, toBeXORed)
    
    return res

tests = [(0, 3), (17, 4), (0, 0), (10, 4), (0, 4), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]

for test in tests:
    print(f"start: {test[0]}, length: {test[1]}, output: {solution(test[0], test[1])}")