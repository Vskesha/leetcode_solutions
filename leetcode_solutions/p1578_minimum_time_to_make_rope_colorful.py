from itertools import groupby
from typing import List


class Solution:
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


class Solution1:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        for k, g in groupby(range(len(colors)), key=lambda x: colors[x]):
            costs = list(map(lambda x: neededTime[x], g))
            ans += sum(costs) - max(costs)
        return ans


class Solution2:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = sum(neededTime)
        for k, g in groupby(range(len(colors)), key=lambda x: colors[x]):
            ans -= max(map(lambda x: neededTime[x], g))
        return ans


class Solution3:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        return sum(neededTime) - sum(
            max(map(lambda j: neededTime[j], g))
            for _, g in groupby(range(len(colors)), key=lambda i: colors[i])
        )


def test_min_cost():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]) == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.minCost(colors="abc", neededTime=[1, 2, 3]) == 0
    print("OK")

    print("Test 3... ", end="")
    assert sol.minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]) == 2
    print("OK")


if __name__ == "__main__":
    test_min_cost()
