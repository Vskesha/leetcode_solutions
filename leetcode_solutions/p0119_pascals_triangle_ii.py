from itertools import pairwise
from math import comb
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex, i) for i in range(rowIndex + 1)]


class Solution1:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            new = [1]
            for j in range(1, len(ans)):
                new.append(ans[j] + ans[j - 1])
            new.append(1)
            ans = new
        return ans


class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            ans = [1] + [a + b for a, b in pairwise(ans)] + [1]
        return ans


def test():
    sol = Solution()

    print("Test 1 ...", end="")
    assert sol.getRow(rowIndex=3) == [1, 3, 3, 1]
    print("ok")

    print("Test 2 ...", end="")
    assert sol.getRow(rowIndex=0) == [1]
    print("ok")

    print("Test 3 ...", end="")
    assert sol.getRow(rowIndex=1) == [1, 1]
    print("ok")


if __name__ == "__main__":
    test()
