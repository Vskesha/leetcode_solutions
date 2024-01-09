from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 for a, b in zip(heights, sorted(heights)) if a != b)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.heightChecker(heights=[1, 1, 4, 2, 1, 3]) == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.heightChecker(heights=[5, 1, 2, 3, 4]) == 5
    print("OK")

    print("Test 3... ", end="")
    assert sol.heightChecker(heights=[1, 2, 3, 4, 5]) == 0
    print("OK")


if __name__ == "__main__":
    test()
