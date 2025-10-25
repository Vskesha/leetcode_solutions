import unittest
from itertools import groupby
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        prev = colors[0]
        pi = 0

        for i in range(1, len(colors)):
            curr = colors[i]
            if curr == prev:
                if neededTime[i] < neededTime[pi]:
                    ans += neededTime[i]
                else:
                    ans += neededTime[pi]
                    pi = i
            else:
                pi = i
            prev = curr

        return ans


class Solution1:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        for _, gr in groupby(range(len(colors)), key=lambda x: colors[x]):
            costs = [neededTime[i] for i in gr]
            ans += sum(costs) - max(costs)
        return ans


class Solution2:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        lc = len(colors)
        i = 0
        ans = 0
        while i < lc:
            c = colors[i]
            m = neededTime[i]
            i += 1
            while i < lc and colors[i] == c:
                if neededTime[i] > m:
                    ans += m
                    m = neededTime[i]
                else:
                    ans += neededTime[i]
                i += 1
        return ans


class Solution3:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        for k, g in groupby(range(len(colors)), key=lambda x: colors[x]):
            costs = list(map(lambda x: neededTime[x], g))
            ans += sum(costs) - max(costs)
        return ans


class Solution4:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = sum(neededTime)
        for k, g in groupby(range(len(colors)), key=lambda x: colors[x]):
            ans -= max(map(lambda x: neededTime[x], g))
        return ans


class Solution5:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        return sum(neededTime) - sum(
            max(map(lambda j: neededTime[j], g))
            for _, g in groupby(range(len(colors)), key=lambda i: colors[i])
        )


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_cost_1(self):
        print("Test minCost 1... ", end="")
        self.assertEqual(
            3, self.sol.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5])
        )
        print("OK")

    def test_min_cost_2(self):
        print("Test minCost 2... ", end="")
        self.assertEqual(
            0, self.sol.minCost(colors="abc", neededTime=[1, 2, 3])
        )
        print("OK")

    def test_min_cost_3(self):
        print("Test minCost 3... ", end="")
        self.assertEqual(
            2, self.sol.minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1])
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
