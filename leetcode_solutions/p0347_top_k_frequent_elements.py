import unittest
from collections import Counter
from heapq import heapify, heappop
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x, _ in Counter(nums).most_common(k)]


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1

        mc = [(-q, n) for n, q in cnt.items()]
        heapify(mc)

        return [heappop(mc)[1] for _ in range(k)]


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = dict()
        for n in nums:
            if n in vals:
                vals[n] += 1
            else:
                vals[n] = 1

        result = [0] * k
        for i in range(k):
            max_count = 0
            for k, c in vals.items():
                if c > max_count:
                    max_count = c
                    result[i] = k
            del vals[result[i]]

        return result


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def assertSameElements(self, a: List[int], b: List[int]):
        self.assertSetEqual(set(a), set(b))

    def test_top_k_frequent_1(self):
        print("test topKFrequent 1... ", end="")
        self.assertSameElements(
            self.sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2), [1, 2]
        )
        print("OK")

    def test_top_k_frequent_2(self):
        print("test topKFrequent 2... ", end="")
        self.assertSameElements(self.sol.topKFrequent(nums=[1], k=1), [1])
        print("OK")


if __name__ == "__main__":
    unittest.main()
