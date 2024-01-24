from time import time
from sys import setrecursionlimit
"""
Operations:
1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (only even)

13 -> 14 -> 7 -> 8 -> 4 -> 2 -> 1
13 -> 12 -> 6 -> 3 -> 2 -> 1
13 -> 12 -> 6 -> 3 -> 4 -> 2 -> 1

15 -> 14 -> 7 -> 8 -> 4 -> 2 -> 1
15 -> 16 -> 8 -> 4 -> 2 -> 1
"""

def solution(n):
    global memoDict
    memoDict = dict()
    setrecursionlimit(10 ** 6)
    return recurse(int(n), memoDict)

def recurse(n, memoDict):
    if n == 1:
        return 0
    
    if n in memoDict:
        return memoDict[n]

    # bitwise check for even
    elif n & 1 == 0:
        memoDict[n] = 1 + recurse(n >> 1, memoDict)
        return memoDict[n]
    
    memoDict[n] = 1 + min(recurse(n - 1, memoDict), recurse(n + 1, memoDict))
    return memoDict[n]

tests = [(4, 2), (15, 5), (13, 5), (173, 11), (123456789 + 10 ** 300, 1242)]
for test in tests:
    start = time()
    print(f'solution({test[0]}) = {solution(test[0])} (expected {test[1]}) -- {time() - start} seconds')