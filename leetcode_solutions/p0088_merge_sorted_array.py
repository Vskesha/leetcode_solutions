import unittest
from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


class Solution2:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy1 = nums1[:m]
        i = j = 0
        for k in range(m + n):
            if i < m and (j >= n or copy1[i] < nums2[j]):
                nums1[k] = copy1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_merge_1(self):
        print("Test merge 1... ", end="")
        nums1 = [1, 2, 3, 0, 0, 0]
        self.sol.merge(nums1=nums1, m=3, nums2=[2, 5, 6], n=3)
        self.assertListEqual(nums1, [1, 2, 2, 3, 5, 6])
        print("OK")

    def test_merge_2(self):
        print("Test merge 2... ", end="")
        nums1 = [1]
        self.sol.merge(nums1=nums1, m=1, nums2=[], n=0)
        self.assertListEqual(nums1, [1])
        print("OK")

    def test_merge_3(self):
        print("Test merge 3... ", end="")
        nums1 = [0]
        self.sol.merge(nums1=nums1, m=0, nums2=[1], n=1)
        self.assertListEqual(nums1, [1])
        print("OK")


if __name__ == "__main__":
    unittest.main()
