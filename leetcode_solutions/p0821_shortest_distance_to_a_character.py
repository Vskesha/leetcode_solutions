from itertools import pairwise
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ls = len(s)
        inds = [i for i in range(ls) if s[i] == c]
        ans = [0] * ls

        st = inds[0]
        for i in range(st):
            ans[i] = st - i

        for i1, i2 in pairwise(inds):
            for i in range(1, (i2 - i1) // 2 + 1):
                ans[i1 + i] = i
                ans[i2 - i] = i

        end = inds[-1]
        for i in range(end + 1, ls):
            ans[i] = i - end

        return ans


class Solution2:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ls = len(s)
        ans = []

        curr = float("inf")
        for i in range(ls):
            curr = 0 if s[i] == c else curr + 1
            ans.append(curr)
        for i in range(ls - 1, -1, -1):
            curr = 0 if s[i] == c else curr + 1
            ans[i] = min(ans[i], curr)

        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.shortestToChar(s="loveleetcode", c="e") == [
        3,
        2,
        1,
        0,
        1,
        0,
        0,
        1,
        2,
        2,
        1,
        0,
    ]
    print("OK")

    print("Test 2... ", end="")
    assert sol.shortestToChar(s="aaab", c="b") == [3, 2, 1, 0]
    print("OK")


if __name__ == "__main__":
    test()
