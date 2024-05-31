from collections import Counter
from heapq import heappush, heappop
from typing import List


class Solution:
    def largestValsFromLabels(
        self, values: List[int], labels: List[int], numWanted: int, useLimit: int
    ) -> int:
        pairs = sorted(zip(values, labels), reverse=True)
        ln = len(values)
        cnt = Counter()
        ans = 0

        for val, lbl in pairs:
            if cnt[lbl] < useLimit:
                ans += val
                cnt[lbl] += 1
                numWanted -= 1
                if not numWanted:
                    break

        return ans


class Solution2:
    def largestValsFromLabels(
        self, values: List[int], labels: List[int], numWanted: int, useLimit: int
    ) -> int:
        heap = []
        for value, label in zip(values, labels):
            heappush(heap, (-value, label))

        cnt = Counter()
        ans = 0

        while heap and numWanted:
            value, label = heappop(heap)
            if cnt[label] < useLimit:
                ans -= value
                numWanted -= 1
                cnt[label] += 1

        return ans


def test_largest_vals_from_labels():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.largestValsFromLabels(
            values=[5, 4, 3, 2, 1], labels=[1, 1, 2, 2, 3], numWanted=3, useLimit=1
        )
        == 9
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.largestValsFromLabels(
            values=[5, 4, 3, 2, 1], labels=[1, 3, 3, 3, 2], numWanted=3, useLimit=2
        )
        == 12
    )
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.largestValsFromLabels(
            values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], numWanted=3, useLimit=1
        )
        == 16
    )
    print("OK")


if __name__ == "__main__":
    test_largest_vals_from_labels()
