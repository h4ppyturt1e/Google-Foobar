
from functools import reduce


def solution(start, length):
    if length == 0:
        return 0
    
    toBeXORed = []
    originalLength = length
    for i in range(originalLength):
        toBeXORed.extend(list(range(start, start + length - i)))
        start += length
        # length -= 1
    
    # XOR all the numbers in the list
    # print(toBeXORed)
    res = reduce(lambda x, y: x ^ y, toBeXORed)
    
    return res

tests = [(0, 3), (17, 4), (0, 0), (10, 4), (0, 4), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]

for test in tests:
    print(f"start: {test[0]}, length: {test[1]}, output: {solution(test[0], test[1])}")