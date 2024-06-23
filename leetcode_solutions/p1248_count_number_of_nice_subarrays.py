import unittest
from collections import deque
from itertools import pairwise
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        indexes = [-1] + [i for i, n in enumerate(nums) if n % 2] + [len(nums)]
        groups = [a - b for a, b in pairwise(indexes)]
        return sum(a * b for a, b in zip(groups, groups[k:]))


class Solution1:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        idx = [-1] + [i for i, n in enumerate(nums) if n % 2] + [len(nums)]
        return sum(
            (b - a) * (d - c) for a, b, c, d in zip(idx, idx[1:], idx[k:], idx[k + 1:])
        )


class Solution2:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        groups = []
        prev = -1

        for i, n in enumerate(nums):
            if n % 2:
                groups.append(i - prev)
                prev = i
        groups.append(len(nums) - prev)

        return sum(a * b for a, b in zip(groups, groups[k:]))


class Solution3:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        que = deque()
        i, pr = 0, -1

        while i < ln and k:
            if nums[i] % 2:
                que.append(i - pr)
                pr = i
                k -= 1
            i += 1

        if k:
            return 0

        i -= 1
        ans = 0
        while i < ln:
            i += 1
            while i < ln and nums[i] % 2 == 0:
                i += 1
            gr = i - pr
            pr = i
            ans += gr * que.popleft()
            que.append(gr)

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_number_of_subarrays_1(self):
        print("Test numberOfSubarrays 1... ", end="")
        self.assertEqual(self.sol.numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3), 2)
        print("OK")

    def test_number_of_subarrays_2(self):
        print("Test numberOfSubarrays 2... ", end="")
        self.assertEqual(self.sol.numberOfSubarrays(nums=[2, 4, 6], k=1), 0)
        print("OK")

    def test_number_of_subarrays_3(self):
        print("Test numberOfSubarrays 3... ", end="")
        self.assertEqual(
            self.sol.numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2), 16
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
