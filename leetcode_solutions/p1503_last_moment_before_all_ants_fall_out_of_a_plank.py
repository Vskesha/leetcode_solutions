from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        r = n - min(right) if right else 0
        l = max(left) if left else 0
        return max(l, r)


class Solution2:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(n - min(right) if right else 0, max(left) if left else 0)


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.getLastMoment(n=4, left=[4, 3], right=[0, 1]) == 4
    print("ok")

    print("Test 2 ... ", end="")
    assert sol.getLastMoment(n=7, left=[], right=[0, 1, 2, 3, 4, 5, 6, 7]) == 7
    print("ok")

    print("Test 3 ... ", end="")
    assert sol.getLastMoment(n=7, left=[0, 1, 2, 3, 4, 5, 6, 7], right=[]) == 7
    print("ok")


if __name__ == "__main__":
    test()
