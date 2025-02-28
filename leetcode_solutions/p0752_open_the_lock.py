from collections import deque
from typing import List


class Solution:
    neibs = {str(n): [str((n + 1) % 10), str((n - 1) % 10)] for n in range(10)}

    def openLock(self, deadends: List[str], target: str) -> int:
        moves = 0
        deadends = set(deadends)

        bfs = deque()
        bfs.append("0000")

        while bfs:
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                if curr == target:
                    return moves
                if curr in deadends:
                    continue
                deadends.add(curr)
                curr = list(curr)
                for i, d in enumerate(curr):
                    ch = curr[i]
                    for neib in Solution.neibs[d]:
                        curr[i] = neib
                        bfs.append("".join(curr))
                    curr[i] = ch

            moves += 1

        return -1


class Solution1:
    neibs = {str(n): [str((n + 1) % 10), str((n - 1) % 10)] for n in range(10)}

    def openLock(self, deadends: List[str], target: str) -> int:
        moves = 0
        deadends = set(deadends)

        bfs = deque()
        bfs.append("0000")

        while bfs:
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                if curr == target:
                    return moves
                if curr in deadends:
                    continue
                deadends.add(curr)
                for i, d in enumerate(curr):
                    st, en = curr[:i], curr[i + 1 :]
                    for neib in Solution.neibs[d]:
                        bfs.append(st + neib + en)
            moves += 1

        return -1


class Solution2:
    neibs = {str(n): [str((n + 1) % 10), str((n - 1) % 10)] for n in range(10)}

    def openLock(self, deadends: List[str], target: str) -> int:
        moves = 0
        deadends = set(deadends)

        bfs = deque()
        bfs.append("0000")

        while bfs:
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                if curr == target:
                    return moves
                if curr in deadends:
                    continue
                deadends.add(curr)
                for i, d in enumerate(curr):
                    for neib in Solution.neibs[d]:
                        bfs.append(curr[:i] + neib + curr[i + 1 :])

            moves += 1

        return -1


class Solution3:
    neibs = {str(n): [str((n + 1) % 10), str((n - 1) % 10)] for n in range(10)}

    def openLock(self, deadends: List[str], target: str) -> int:
        moves = 0
        deadends = set(deadends)

        bfs = deque()
        bfs.append("0000")

        while bfs:
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                if curr == target:
                    return moves
                if curr in deadends:
                    continue
                deadends.add(curr)
                for i, d in enumerate(curr):
                    for neib in Solution.neibs[d]:
                        cr = list(curr)
                        cr[i] = neib
                        bfs.append("".join(cr))

            moves += 1

        return -1


def test_open_lock():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.openLock(deadends=["8888"], target="0009") == 1
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.openLock(
            deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
            target="8888",
        )
        == -1
    )
    print("OK")


if __name__ == "__main__":
    test_open_lock()
