

def solution(id, base):
    # print(id, base)
    seen, last_id = recurse(id, base, dict())
    return getLongestChain(last_id, seen)

def getLongestChain(last_id, seen):
    if seen[last_id] == last_id:
        return 1
    
    repeats = 0
    
    visited = set()
    
    while True:
        if last_id in visited:
            break
        repeats += 1
        visited.add(last_id)
        last_id = seen[last_id]
    
    return repeats
    

def recurse(id, base, seen):
    if id in seen:
        return seen, id
    
    k = len(id)
    x = "".join(sorted(id, reverse=True))
    y = "".join(sorted(id))
    z = subtractInBase(str(x), str(y), base)
    # print(x, y, z)
    
    if len(str(z)) < k:
        z = str(z).zfill(k)
    
    seen[id] = z
    # print(seen)
    return recurse(str(z), base, seen)

def subtractInBase(x, y, base):
    borrow = 0
    result = []
    for i in range(1, len(x) + 1):
        d = int(x[-i]) - int(y[-i]) - borrow
        if d < 0:
            d += base
            borrow = 1
        else:
            borrow = 0
        result.append(str(d))
    return ''.join(reversed(result))


tests = [("1211", 10, 1), ("210022", 3, 3)]

for test in tests:
    print(solution(test[0], test[1]) == test[2])