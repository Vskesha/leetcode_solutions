import unittest
from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nmin = min(nums)
        size = max(nums) - nmin + 2
        bitree = [0] * size
        ln = len(nums)
        counts = [0] * ln

        for i in range(ln - 1, -1, -1):
            k = nums[i] - nmin
            n = k + 1
            while k > 0:
                counts[i] += bitree[k]
                k -= k & (-k)
            while n < size:
                bitree[n] += 1
                n += n & (-n)

        return counts

class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nmin = min(nums)
        nmax = max(nums)
        size = nmax - nmin + 2
        bitree = [0] * size

        def update(i, diff):
            while i < size:
                bitree[i] += diff
                i += i & (-i)

        def get_sum(i):
            ans = 0
            while i > 0:
                ans += bitree[i]
                i -= i & (-i)
            return ans

        ln = len(nums)
        counts = [0] * ln

        for i in range(ln - 1, -1, -1):
            num = nums[i] - nmin + 1
            counts[i] = get_sum(num - 1)
            update(num, 1)

        return counts


class BITree:
    def __init__(self, size):
        self.tree = [0] * size

    def update(self, i, diff):
        while i < len(self.tree):
            self.tree[i] += diff
            i += i & (-i)

    def get_sum(self, i):
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= i & (-i)
        return ans


class Solution3:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nmin = min(nums)
        nmax = max(nums)
        size = nmax - nmin + 2
        bitree = BITree(size)
        ln = len(nums)
        counts = [0] * ln

        for i in range(ln - 1, -1, -1):
            num = nums[i] - nmin + 1
            counts[i] = bitree.get_sum(num - 1)
            bitree.update(num, 1)

        return counts


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_countSmaller_1(self):
        print("Test countSmaller 1... ", end="")
        self.assertListEqual([2, 1, 1, 0], self.sol.countSmaller(nums=[5, 2, 6, 1]))
        print("OK")

    def test_countSmaller_2(self):
        print("Test countSmaller 2... ", end="")
        self.assertListEqual([0], self.sol.countSmaller(nums=[-1]))
        print("OK")

    def test_countSmaller_3(self):
        print("Test countSmaller 3... ", end="")
        self.assertListEqual([0, 0], self.sol.countSmaller(nums=[-1, -1]))
        print("OK")


if __name__ == "__main__":
    unittest.main()
