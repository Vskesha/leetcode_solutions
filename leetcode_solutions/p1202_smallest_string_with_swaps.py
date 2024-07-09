import unittest
from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parents = list(range(n))

        def find(node):  # find root
            if node == parents[node]:
                return node
            parents[node] = find(parents[node])
            return parents[node]

        for node1, node2 in pairs:
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                parents[root2] = root1

        sets = defaultdict(list)
        for i in range(n):
            sets[find(i)].append(i)

        ans = [""] * n
        for indices in sets.values():
            chars = []
            for i in indices:
                chars.append(s[i])
            for i, char in zip(sorted(indices), sorted(chars)):
                ans[i] = char

        return "".join(ans)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_smallest_string_with_swaps_1(self):
        print("Test smallestStringWithSwaps 1... ", end="")
        self.assertEqual(
            self.sol.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]), "bacd"
        )
        print("OK")

    def test_smallest_string_with_swaps_2(self):
        print("Test smallestStringWithSwaps 2... ", end="")
        self.assertEqual(
            self.sol.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]),
            "abcd",
        )
        print("OK")

    def test_smallest_string_with_swaps_3(self):
        print("Test smallestStringWithSwaps 3... ", end="")
        self.assertEqual(
            self.sol.smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]), "abc"
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
