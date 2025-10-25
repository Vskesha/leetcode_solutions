from bisect import bisect_left
from itertools import accumulate
from random import randint
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.sums = list(accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.sums, randint(1, self.sums[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


def test():
    sol = Solution()


if __name__ == "__main__":
    test()
