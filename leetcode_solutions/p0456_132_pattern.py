from itertools import accumulate
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mins = list(accumulate(nums, min))
        stack = []
        for mk, nk in zip(mins[::-1], nums[::-1]):
            if nk == mk:
                continue
            while stack and stack[-1] <= mk:
                stack.pop()
            if stack and nk > stack[-1]:
                return True
            else:
                stack.append(nk)
        return False


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.find132pattern([1, 2, 3, 4]) is False
    print("ok")
    print("Test 2 ... ", end="")
    assert sol.find132pattern([3, 1, 4, 2]) is True
    print("ok")
    print("Test 3 ... ", end="")
    assert sol.find132pattern([-1, 3, 2, 0]) is True
    print("ok")
    print("Test 4 ... ", end="")
    assert sol.find132pattern([1, 0, 1, -4, -3]) is False
    print("ok")
    print("Test 5 ... ", end="")
    assert sol.find132pattern(nums=[1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) is True
    print("ok")


if __name__ == "__main__":
    test()
