from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    tmp = "123456789"
    nums = []
    for i in range(1, 10):
        for st in range(10 - i):
            nums.append(int(tmp[st : st + i]))

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        fr = bisect_left(Solution.nums, low)
        to = bisect_right(Solution.nums, high)
        return Solution.nums[fr:to]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.sequentialDigits(low=100, high=300) == [123, 234]
    print("OK")

    print("Test 2... ", end="")
    assert sol.sequentialDigits(low=1000, high=13000) == [
        1234,
        2345,
        3456,
        4567,
        5678,
        6789,
        12345,
    ]
    print("OK")


if __name__ == "__main__":
    test()
