import unittest
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())


class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        n1, n2 = sorted(nums1), sorted(nums2)
        i, l2, result = 0, len(n2), []
        for n in n1:
            while i < l2 and n2[i] < n:
                i += 1
            if i >= l2:
                break
            if n2[i] == n:
                result.append(n)
                i += 1
        return result


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def same_values(self, a, b):
        self.assertEqual(a, b)

    def test_intersect_1(self):
        print("test intersect 1 ... ", end="")
        self.same_values(
            self.sol.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]), [2, 2]
        )
        print("OK")

    def test_intersect_2(self):
        print("test intersect 2 ... ", end="")
        self.same_values(
            self.sol.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]), [4, 9]
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
