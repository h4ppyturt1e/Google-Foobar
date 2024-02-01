import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        entrances = [0]
        exits = [3]
        path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
        expected_output = 6
        self.assertEqual(solution(entrances, exits, path), expected_output)

    def test_case2(self):
        entrances = [0, 1]
        exits = [4, 5]
        path = [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        expected_output = 16
        self.assertEqual(solution(entrances, exits, path), expected_output)

if __name__ == '__main__':
    unittest.main()