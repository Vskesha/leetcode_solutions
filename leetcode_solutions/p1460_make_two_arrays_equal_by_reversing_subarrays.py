from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


def test_can_be_equal():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]) is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.canBeEqual(target=[7], arr=[7]) is True
    print("OK")

    print("Test 3... ", end="")
    assert sol.canBeEqual(target=[3, 7, 9], arr=[3, 7, 11]) is False
    print("OK")


if __name__ == "__main__":
    test_can_be_equal()
