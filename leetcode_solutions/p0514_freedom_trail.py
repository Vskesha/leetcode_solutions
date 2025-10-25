from collections import defaultdict
from heapq import heappop, heappush
from math import inf


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        lr = len(ring)

        ring_indices = defaultdict(list)
        for i, ch in enumerate(ring):
            ring_indices[ch].append(i)

        moves = {0: 0}
        for ch in key:
            moves = {
                ri: min(
                    mv + min(dist := (ri - pri) % lr, lr - dist) + 1
                    for pri, mv in moves.items()
                )
                for ri in ring_indices[ch]
            }

        return min(moves.values())


class Solution1:
    def findRotateSteps(self, ring: str, key: str) -> int:
        lr, lk = len(ring), len(key)

        ring_indices = defaultdict(list)
        for i, ch in enumerate(ring):
            ring_indices[ch].append(i)

        moves = {0: 0}
        for ch in key:
            new = {}
            for ri in ring_indices[ch]:
                new[ri] = float("inf")
                for pri, mv in moves.items():
                    dist = (ri - pri) % lr
                    dist = min(dist, lr - dist)
                    new[ri] = min(new[ri], mv + dist + 1)
            moves = new

        return min(moves.values())


class Solution2:
    def findRotateSteps(self, ring: str, key: str) -> int:
        lr = len(ring)
        lk = len(key)
        ring_indices = defaultdict(list)
        for i, ch in enumerate(ring):
            ring_indices[ch].append(i)

        heap = [(0, 0, 0)]
        moves = [[inf] * lr for _ in range(lk + 1)]

        while True:
            mv, ri, ki = heappop(heap)
            if ki == lk:
                return mv
            if mv > moves[ki][ri]:
                continue
            ch = key[ki]
            ki += 1
            for idx in ring_indices[ch]:
                dist = (ri - idx) % lr
                dist = min(dist, lr - dist)
                mvc = mv + dist + 1
                if moves[ki][idx] > mvc:
                    heappush(heap, (mvc, idx, ki))
                    moves[ki][idx] = mvc


def test_find_rotate_steps():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findRotateSteps(ring="godding", key="gd") == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.findRotateSteps(ring="godding", key="godding") == 13
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.findRotateSteps(
            ring="caotmcaataijjxi",
            key="oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx",
        )
        == 137
    )
    print("OK")


if __name__ == "__main__":
    test_find_rotate_steps()
