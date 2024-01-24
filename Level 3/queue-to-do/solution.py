def solution(start, length):
    if length == 0:
        return 0
    
    res = 0
    originalLength = length
    for i in range(originalLength):
        xor = getXORRange(start, start + length - i - 1)
        start += length
        res ^= xor
        
    return res

def getXORRange(start, end):
    # get 0 to start - 1
    zeroToStart = -1
    if (start - 1) % 4 == 0:
        zeroToStart = start - 1
    elif (start - 1) % 4 == 1:
        zeroToStart = 1
    elif (start - 1) % 4 == 2:
        zeroToStart = start
    else: # (start - 1) % 4 == 3:
        zeroToStart = 0
    
    # get 0 to end
    zeroToEnd = -1
    if end % 4 == 0:
        zeroToEnd = end
    elif end % 4 == 1:
        zeroToEnd = 1
    elif end % 4 == 2:
        zeroToEnd = end + 1
    else: # end % 4 == 3:
        zeroToEnd = 0
    
    return zeroToStart ^ zeroToEnd
    
    
tests = [(0, 3), (17, 4), (0, 0), (10, 4), (0, 4), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]

for test in tests:
    print(f"start: {test[0]}, length: {test[1]}, output: {solution(test[0], test[1])}")