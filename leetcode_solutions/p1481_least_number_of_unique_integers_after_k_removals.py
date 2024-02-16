from collections import Counter
from heapq import heapify, heappop
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        vals = sorted(Counter(arr).values())
        for i, n in enumerate(vals):
            if n > k:
                return len(vals) - i
            else:
                k -= n
        return 0


class Solution1:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        vals = sorted(Counter(arr).values())
        heapify(vals)
        while vals and k >= vals[0]:
            k -= heappop(vals)
        return len(vals)


class Solution2:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        vals = sorted(Counter(arr).values(), reverse=True)
        while vals and vals[-1] <= k:
            k -= vals.pop()
        return len(vals)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1) == 1
    print("OK")

    print("Test 2... ", end="")
    assert sol.findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3) == 2
    print("OK")


if __name__ == "__main__":
    test()
