from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))


def test_distribute_candies():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.distributeCandies(candyType=[1, 1, 2, 2, 3, 3]) == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.distributeCandies(candyType=[1, 1, 2, 3]) == 2
    print("OK")

    print("Test 3... ", end="")
    assert sol.distributeCandies(candyType=[6, 6, 6, 6]) == 1
    print("OK")


if __name__ == "__main__":
    test_distribute_candies()
