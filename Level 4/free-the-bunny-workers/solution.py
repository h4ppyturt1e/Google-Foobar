"""
locks [0-end]
each bunny gets keys
    - list of
        - sorted list of the numbers for the keys

solution
    - sorted list of each bunny's list of keys
    - lexicographically least such key distribution
        - first bunny should have keys sequentially from 0

num_buns - [1-9]
num_required - [0-9]

Ex.
solution(3, 1)
(3 bunnies, 1 needed to open)

Any of the 3 bunnies can open
[[0],  [0],  [0]]

solution(2, 2)
(2 bunnies, 2 needed to open)

Each bunny needs 1 
[[0], [1]]

solution(3, 2)
(3 bunnies, 2 needed to open)

Any 2 bunnies can open
[[0, 1], [0, 2], [1, 2]]
"""

from itertools import combinations

def solution(num_buns, num_required):
    # # if num_required == 0, return no keys
    # if num_required == 0:
    #     return [[] for _ in range(num_buns)]

    # # equal to the number of keys each bunny has
    # if num_buns == num_required:
    #     return [[i] for i in range(num_buns)]

    # # if only 1 required, each bunny has a key
    # if num_required == 1:
    #     return [[0] for _ in range(num_buns)]

    soln = [[] for _ in range(num_buns)]

    overallCombos = list(combinations(range(num_buns), num_buns - num_required + 1))

    # print(f"overallCombos ({len(overallCombos)}): {overallCombos}")
    
    for key, order in enumerate(overallCombos):
        for i in order:
            soln[i].append(key)

    return soln


def printFormatted(soln):
    for i in range(len(soln)):
        print(f'{i}: {soln[i]}')


tests = [
    # ((3, 1), [[0], [0], [0]]),
    # ((2, 2), [[0], [1]]),
    # ((3, 2), [[0, 1], [0, 2], [1, 2]]),
    # ((4, 4), [[0], [1], [2], [3]]),
    # ((2, 1), [[0], [0]]),
    # ((5, 3), [[0, 1, 2, 3, 4, 5],
    #           [0, 1, 2, 6, 7, 8],
    #           [0, 3, 4, 6, 7, 9],
    #           [1, 3, 5, 6, 8, 9],
    #           [2, 4, 5, 7, 8, 9]])
]

# Additional test cases written by ChatGPT4
additional_tests = [
    # Only one bunny, no keys required
    ((1, 0), [[]]),
    
    # Only one bunny, one key required
    ((1, 1), [[0]]),

    # Two bunnies, one required
    ((2, 1), [[0], [0]]),

    # Two bunnies, both required
    ((2, 2), [[0], [1]]),

    # Four bunnies, three required
    ((4, 3), [[0, 1, 2],
              [0, 1, 3],
              [0, 2, 3],
              [1, 2, 3]]),

    # Five bunnies, four required
    ((5, 4), [[0, 1, 2, 3],
              [0, 1, 2, 4],
              [0, 1, 3, 4],
              [0, 2, 3, 4],
              [1, 2, 3, 4]]),

    # Maximum number of bunnies, minimum keys required
    ((9, 1), [[0], [0], [0], [0], [0], [0], [0], [0], [0]]),

    # One bunny, multiple keys required (impossible case)
    ((1, 3), []),

    # Number of keys required exceeds number of bunnies (impossible case)
    ((3, 5), []),

    # All bunnies required
    ((5, 5), [[0], [1], [2], [3], [4]]),

    # Large number of bunnies with specific key requirement
    ((7, 3), [[0, 1, 2, 3, 4, 5], 
              [0, 1, 2, 6, 7, 8], 
              [0, 1, 3, 6, 7, 9], 
              [0, 2, 3, 6, 8, 9], 
              [1, 2, 3, 7, 8, 9], 
              [1, 4, 5, 6, 8, 9], 
              [2, 4, 5, 7, 8, 9]]),

    # No bunnies, no keys required (edge case)
    ((0, 0), []),

    # All bunnies, no keys required
    ((9, 0), [[], [], [], [], [], [], [], [], []]),
]

# Test Case 1: High number of bunnies but a low number required to open locks
# Expectations are that each key is duplicated among different bunnies to ensure any single bunny can open the locks.
test_1 = ((6, 1), [[0], [0], [0], [0], [0], [0]])

# Test Case 2: A moderate number of bunnies and exactly half are required to open locks
# This configuration should distribute keys more evenly, ensuring every combination of half the bunnies can open the locks.
test_2 = ((4, 2), [[0, 1, 2], [0, 3, 4], [1, 3, 5], [2, 4, 5]])

# Test Case 3: Large number of bunnies with most required to open locks
# Such a scenario is closer to a scenario where nearly all bunnies are needed, thus more specific key distribution.
test_3 = ((7, 6), [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 6], [0, 1, 2, 3, 5, 6], [
          0, 1, 2, 4, 5, 6], [0, 1, 3, 4, 5, 6], [0, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]])

# Test Case 4: Many bunnies, only a few required
# This is another extreme case where only a few are needed but there are many bunnies to distribute keys amongst.
test_4 = ((5, 2), [[0, 1, 2, 3], [0, 4, 5, 6], [1, 4, 7, 8], [2, 5, 7, 9], [3, 6, 8, 9]])

# Test Case 5: Equally required as bunnies
# This should result in each bunny holding a unique key.
test_5 = ((8, 8), [[0], [1], [2], [3], [4], [5], [6], [7]])

# Test Case 6: All bunnies can open with no keys required
# This represents a situation where no bunny needs a key to open locks.
test_6 = ((4, 0), [[], [], [], []])

# Test Case 7: One bunny, one key required
# The simplest of cases where one bunny needs one key.
test_7 = ((1, 1), [[0]])

tests.extend([
              test_1,
              test_2, 
              test_3, 
              test_4, 
              test_5, 
              test_6, 
              test_7,
              ])

tests.extend(additional_tests)

for test in tests:
    num_buns, num_required = test[0]
    expected = test[1]
    res = solution(num_buns, num_required)

    if res != expected:
        print("\nRunning test for solution({0}, {1})...".format(
            num_buns, num_required))
        print("solution({0}, {1}):\n".format(num_buns, num_required))
        printFormatted(res)
        print("\nExpected:\n")
        printFormatted(expected)
