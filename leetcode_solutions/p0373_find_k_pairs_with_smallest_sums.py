import unittest
from heapq import heappop, heappush
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]
        result = []
        l1, l2 = len(nums1) - 1, len(nums2) - 1

        for _ in range(k):
            _, i, j = heappop(heap)
            result.append([nums1[i], nums2[j]])
            if i < l1:
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            if not i and j < l2:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result


class Solution2:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]
        n1, n2 = len(nums1), len(nums2)
        res = []

        while heap and k:
            minimum = heappop(heap)
            _, i, j = minimum
            res.append([nums1[i], nums2[j]])
            if j < n2 - 1:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0 and i < n1 - 1:
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            k -= 1
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    @staticmethod
    def same_lists(list1, list2) -> bool:
        return set(map(tuple, list1)) == set(map(tuple, list2))

    def test_k_smallest_pairs_1(self):
        print("Test kSmallestPairs 1... ", end="")
        self.assertTrue(
            self.same_lists(
                self.sol.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3),
                [[1, 2], [1, 4], [1, 6]],
            )
        )
        print("OK")

    def test_k_smallest_pairs_2(self):
        print("Test kSmallestPairs 2... ", end="")
        self.assertTrue(
            self.same_lists(
                self.sol.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2),
                [[1, 1], [1, 1]],
            )
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
