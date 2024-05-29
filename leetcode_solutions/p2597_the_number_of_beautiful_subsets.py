from collections import defaultdict
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        cant_place = defaultdict(set)

        for i in range(1, ln):
            for j in range(i):
                if abs(nums[i] - nums[j]) == k:
                    cant_place[i].add(j)

        def backtrack(i, comb):
            if i == ln:
                if comb:
                    self.bs += 1
                return

            backtrack(i + 1, comb)
            if not comb & cant_place[i]:
                comb.add(i)
                backtrack(i + 1, comb)
                comb.remove(i)

        self.bs = 0
        backtrack(0, set())
        return self.bs


def test_beautiful_subsets():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.beautifulSubsets(nums=[2, 4, 6], k=2) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.beautifulSubsets(nums=[1], k=1) == 1
    print("OK")


if __name__ == "__main__":
    test_beautiful_subsets()
