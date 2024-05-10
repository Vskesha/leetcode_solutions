from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = [(arr[0] / arr[i], 0, i) for i in range(1, len(arr))]
        heapify(heap)
        for _ in range(k - 1):
            _, eni, dei = heappop(heap)
            heappush(heap, (arr[eni + 1] / arr[dei], eni + 1, dei))
        _, eni, dei = heappop(heap)
        return [arr[eni], arr[dei]]


class Solution2:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = [(arr[0] / arr[i], 0, i) for i in range(1, len(arr))]
        heapify(heap)

        for _ in range(k - 1):
            _, eni, dei = heappop(heap)
            eni += 1
            if eni < dei:
                heappush(heap, (arr[eni] / arr[dei], eni, dei))

        _, eni, dei = heappop(heap)
        return [arr[eni], arr[dei]]


def test_kth_smallest_prime_fraction():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3) == [2, 5]
    print("OK")

    print("Test 2... ", end="")
    assert sol.kthSmallestPrimeFraction(arr=[1, 7], k=1) == [1, 7]
    print("OK")


if __name__ == "__main__":
    test_kth_smallest_prime_fraction()
