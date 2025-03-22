from heapq import heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])

        def summ(indices):
            return sum(mat[r][c] for r, c in enumerate(indices))

        lowest = tuple([0] * m)
        heap = [(summ(lowest), lowest)]
        visited = set()
        visited.add(lowest)
        csum = 0
        n -= 1
        for _ in range(k):
            csum, indices = heappop(heap)
            indices = list(indices)
            for r, c in enumerate(indices):
                if c != n:
                    indices[r] = c + 1
                new_indices = tuple(indices)
                if new_indices not in visited:
                    heappush(heap, (summ(new_indices), new_indices))
                    visited.add(new_indices)
                indices[r] = c

        return csum


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])

        def one_pair(curr, prev):
            heap = []
            heappush(heap, (curr[0] + prev[0], 0, 0))
            res = []
            lc, lp = len(curr) - 1, len(prev) - 1
            while heap and len(res) < k:
                val, i, j = heappop(heap)
                res.append(val)
                if j == 0 and i != lc:
                    heappush(heap, (curr[i + 1] + prev[0], i + 1, 0))
                if j != lp:
                    heappush(heap, (curr[i] + prev[j + 1], i, j + 1))
            return res

        prev = [0]
        for row in mat:
            prev = one_pair(row, prev)
        return prev[-1]


def test_kth_smallest():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.kthSmallest(mat=[[1, 3, 11], [2, 4, 6]], k=5) == 7
    print("OK")

    print("Test 2... ", end="")
    assert sol.kthSmallest(mat=[[1, 3, 11], [2, 4, 6]], k=9) == 17
    print("OK")

    print("Test 3... ", end="")
    assert sol.kthSmallest(mat=[[1, 10, 10], [1, 4, 5], [2, 3, 6]], k=7) == 9
    print("OK")


if __name__ == "__main__":
    test_kth_smallest()
