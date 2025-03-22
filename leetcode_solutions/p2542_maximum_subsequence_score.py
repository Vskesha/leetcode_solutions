import bisect
import unittest
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []
        ts = ans = 0

        for n2, n1 in sorted(zip(nums2, nums1), reverse=True):
            heappush(heap, n1)
            ts += n1
            if len(heap) == k:
                ans = max(ans, ts * n2)
                ts -= heappop(heap)

        return ans


class Solution2:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = iter(sorted(zip(nums2, nums1), reverse=True))
        heap = []
        ts = ans = 0

        for _ in range(k - 1):
            _, n1 = next(pairs)
            heappush(heap, n1)
            ts += n1
        for n2, n1 in pairs:
            heappush(heap, n1)
            ts += n1
            ans = max(ans, ts * n2)
            ts -= heappop(heap)

        return ans


class Solution3:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        heap = []
        ts = ans = 0

        for _, n1 in pairs[: k - 1]:
            heappush(heap, n1)
            ts += n1
        for n2, n1 in pairs[k - 1 :]:
            heappush(heap, n1)
            ts += n1
            ans = max(ans, ts * n2)
            ts -= heappop(heap)

        return ans


class Solution4:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs.sort(key=lambda x: x[1], reverse=True)

        my_heap = []
        for i in range(k):
            bisect.insort(my_heap, pairs[i][0])

        heap_sum = sum(my_heap)
        max_score = heap_sum * pairs[k - 1][1]
        for i in range(k, len(pairs)):
            curr_val = pairs[i][0]
            curr_min = pairs[i][1]
            bisect.insort(my_heap, curr_val)
            heap_sum += curr_val - my_heap.pop(0)
            max_score = max(max_score, heap_sum * curr_min)

        return max_score


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_max_score_1(self):
        print("Test maxScore 1... ", end="")
        self.assertEqual(
            self.sol.maxScore(nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3), 12
        )
        print("OK")

    def test_max_score_2(self):
        print("Test maxScore 2... ", end="")
        self.assertEqual(
            self.sol.maxScore(nums1=[4, 2, 3, 1, 1], nums2=[7, 5, 10, 9, 6], k=1), 30
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
