from time import time
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
    return recurse(int(n), memoDict)

def recurse(n, memoDict):
    if n == 1:
        return 0
    
    if n in memoDict:
        return memoDict[n]
    
    # if n is a power of 2, we can just get bits-1
    elif isPow2(n):
        memoDict[n] = int.bit_length(n) - 1
        return memoDict[n]
    
    # bitwise check for even
    elif n & 1 == 0:
        memoDict[n] = 1 + recurse(n >> 1, memoDict)
        return memoDict[n]

    memoDict[n] = 1 + min(recurse(n - 1, memoDict), recurse(n + 1, memoDict))
    return memoDict[n]

def isPow2(n):
    return n > 0 and (n & (n - 1)) == 0

tests = [(4, 2), (15, 5), (123456789 + 10 ** 220, 0)]
for test in tests:
    start = time()
    print(f'solution({test[0]}) = {solution(test[0])} (expected {test[1]}) -- {time() - start} seconds')