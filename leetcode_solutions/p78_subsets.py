from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [list(c) for l in range(len(nums) + 1) for c in combinations(nums, l)]


class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        for length in range(len(nums) + 1):
            for comb in combinations(nums, length):
                ans.append(list(comb))

        return ans


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        ln = len(nums)

        def dp(i, comb):
            if i == ln:
                self.ans.append(comb.copy())
                return

            dp(i + 1, comb)
            comb.append(nums[i])
            dp(i + 1, comb)
            comb.pop()

        dp(0, [])
        return self.ans


class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ln = len(nums)

        def backtrack(i, comb) -> list:
            if i == ln:
                return [comb.copy()]

            res = backtrack(i + 1, comb)

            comb.append(nums[i])
            res.extend(backtrack(i + 1, comb))
            comb.pop()

            return res

        return backtrack(0, [])


def test_subsets():
    sol = Solution()

    print("Test 1... ", end="")
    res = sol.subsets(nums=[1, 2, 3])
    out = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    res = set(tuple(r) for r in res)
    out = set(tuple(r) for r in out)
    assert res == out
    print("OK")

    print("Test 2... ", end="")
    res = sol.subsets(nums=[0])
    out = [[], [0]]
    res = set(tuple(r) for r in res)
    out = set(tuple(r) for r in out)
    assert res == out
    print("OK")


if __name__ == "__main__":
    test_subsets()
