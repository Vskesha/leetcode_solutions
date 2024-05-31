from collections import defaultdict
from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xors = defaultdict(list)
        xors[0].append(-1)
        cxor = 0
        ans = 0

        for i, n in enumerate(arr):
            cxor ^= n
            for st in xors[cxor]:
                ans += i - st - 1
            xors[cxor].append(i)

        return ans


def test_count_triplets():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.countTriplets(arr=[2, 3, 1, 6, 7]) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.countTriplets(arr=[1, 1, 1, 1, 1]) == 10
    print("OK")


if __name__ == "__main__":
    test_count_triplets()
