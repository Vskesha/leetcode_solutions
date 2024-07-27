import unittest
from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        idx = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda n: (idx.get(n, 1001), n))


class Solution2:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        ans = []

        for n in arr2:
            ans.extend([n] * cnt[n])
            del cnt[n]

        for n in sorted(cnt.keys()):
            ans.extend([n] * cnt[n])

        return ans


class Solution3:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        ans = []
        for n in arr2:
            ans.extend([n] * cnt[n])
            del cnt[n]
        ans.extend(sorted(cnt.elements()))
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_relative_sort_array1(self):
        print("Test relativeSortArray 1 ... ", end="")
        self.assertListEqual(
            self.sol.relativeSortArray(
                arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]
            ),
            [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
        )
        print("OK")

    def test_relative_sort_array2(self):
        print("Test relativeSortArray 2 ... ", end="")
        self.assertListEqual(
            self.sol.relativeSortArray(
                arr1=[28, 6, 22, 8, 44, 17], arr2=[22, 28, 8, 6]
            ),
            [22, 28, 8, 6, 17, 44],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
