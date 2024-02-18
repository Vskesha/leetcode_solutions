from heapq import heappush, heappushpop
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        lh = len(heights)
        heap = []
        for i in range(lh - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            if len(heap) < ladders:
                heappush(heap, diff)
                continue
            need = heappushpop(heap, diff)
            if need > bricks:
                return i
            bricks -= need
        return lh - 1


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1) == 4
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.furthestBuilding(
            heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2
        )
        == 7
    )
    print("OK")

    print("Test 3... ", end="")
    assert sol.furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0) == 3
    print("OK")


if __name__ == "__main__":
    test()
