from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[i] for i in range(len(piles) // 3, len(piles), 2))


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.maxCoins(piles=[2, 4, 1, 2, 7, 8]) == 9
    print("OK")

    print("Test 2... ", end="")
    assert sol.maxCoins(piles=[2, 4, 5]) == 4
    print("OK")

    print("Test 3... ", end="")
    assert sol.maxCoins(piles=[9, 8, 7, 6, 5, 1, 2, 3, 4])
    print("OK")


if __name__ == "__main__":
    test()
