from heapq import heapify, heappop
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        aux = []
        for i, row in enumerate(mat):
            aux.append((sum(row), i))
        heapify(aux)
        ans = []
        for _ in range(k):
            ans.append(heappop(aux)[1])
        return ans


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.kWeakestRows(mat=[[1, 1, 0, 0, 0],
                                 [1, 1, 1, 1, 0],
                                 [1, 0, 0, 0, 0],
                                 [1, 1, 0, 0, 0],
                                 [1, 1, 1, 1, 1]],
                             k=3) == [2, 0, 3]
    print('ok\nTest 2 ... ', end='')
    assert sol.kWeakestRows(mat=[[1, 0, 0, 0],
                                 [1, 1, 1, 1],
                                 [1, 0, 0, 0],
                                 [1, 0, 0, 0]],
                            k=2) == [0, 2]
    print('ok')


if __name__ == '__main__':
    test()
