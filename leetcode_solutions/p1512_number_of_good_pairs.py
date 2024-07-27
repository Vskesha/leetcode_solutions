import unittest
from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(n * (n - 1) for n in Counter(nums).values()) // 2


class Solution1:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        counter = Counter(nums)
        for q in counter.values():
            ans += q * (q - 1) // 2
        return ans


class Solution2:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans, cnt = 0, {}
        for n in nums:
            if n in cnt:
                cnt[n] += 1
                ans += cnt[n]
            else:
                cnt[n] = 0
        return ans


class Solution3:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(q * (q - 1) for q in Counter(nums).values()) // 2


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_numIdenticalPairs_1(self):
        print("Test numIdenticalPairs 1... ", end="")
        self.assertEqual(4, self.sol.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
        print("OK")

    def test_numIdenticalPairs_2(self):
        print("Test numIdenticalPairs 2... ", end="")
        self.assertEqual(6, self.sol.numIdenticalPairs(nums=[1, 1, 1, 1]))
        print("OK")

    def test_numIdenticalPairs_3(self):
        print("Test numIdenticalPairs 3... ", end="")
        self.assertEqual(0, self.sol.numIdenticalPairs(nums=[1, 2, 3]))
        print("OK")


if __name__ == "__main__":
    unittest.main()
