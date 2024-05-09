from heapq import heapify, heappop
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0

        for i in range(k):
            h = happiness[i] - i
            if h < 0:
                break
            res += h

        return res


class Solution2:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = [-h for h in happiness]
        heapify(heap)
        res = 0

        for i in range(k):
            h = -heappop(heap) - i
            if h > 0:
                res += h
            else:
                return res

        return res


def test_maximum_happiness_sum():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.maximumHappinessSum(happiness=[1, 2, 3], k=2) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.maximumHappinessSum(happiness=[1, 1, 1, 1], k=2) == 1
    print("OK")

    print("Test 3... ", end="")
    assert sol.maximumHappinessSum(happiness=[2, 3, 4, 5], k=1) == 5
    print("OK")


if __name__ == "__main__":
    test_maximum_happiness_sum()
