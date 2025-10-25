from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        return len(cnt) == len(set(cnt.values()))


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]) is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.uniqueOccurrences(arr=[1, 2]) is False
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) is True
    )
    print("OK")


if __name__ == "__main__":
    test()
