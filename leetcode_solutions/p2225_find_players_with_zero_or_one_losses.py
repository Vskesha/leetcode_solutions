from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = Counter(l for _, l in matches)
        winners = set(w for w, _ in matches) - set(losers)
        losers = [x for x in losers if losers[x] == 1]
        return [sorted(winners), sorted(losers)]


class Solution2:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        return [
            sorted(
                set(w for w, _ in matches)
                - set(losers := Counter(l for _, l in matches))
            ),
            sorted([x for x in losers if losers[x] == 1]),
        ]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    for a, b in zip(
        sol.findWinners(
            matches=[
                [1, 3],
                [2, 3],
                [3, 6],
                [5, 6],
                [5, 7],
                [4, 5],
                [4, 8],
                [4, 9],
                [10, 4],
                [10, 9],
            ]
        ),
        [[1, 2, 10], [4, 5, 7, 8]],
    ):
        assert a == b
    print("OK")

    print("Test 2... ", end="")
    for a, b in zip(
        sol.findWinners(matches=[[2, 3], [1, 3], [5, 4], [6, 4]]), [[1, 2, 5, 6], []]
    ):
        assert a == b
    print("OK")


if __name__ == "__main__":
    test()
