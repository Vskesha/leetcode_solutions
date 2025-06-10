import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def robotWithString(self, s: str) -> str:
        ls = len(s)
        minch = s[-1]
        mins = [minch] * len(s)
        for i in range(ls - 1, -1, -1):
            if s[i] < minch:
                minch = s[i]
            mins[i] = minch

        ans, st = [], []
        for i, ch in enumerate(s):
            while st and st[-1] <= mins[i]:
                ans.append(st.pop())
            st.append(ch)

        while st:
            ans.append(st.pop())
        return "".join(ans)


class Solution2:
    def robotWithString(self, s: str) -> str:
        mstack, st, ans = ["z"], [], []

        for ch in reversed(s):
            if ch <= mstack[-1]:
                mstack.append(ch)

        for ch in s:
            while st and st[-1] <= mstack[-1]:
                ans.append(st.pop())
            if ch == mstack[-1]:
                mstack.pop()
            st.append(ch)

        while st:
            ans.append(st.pop())
        return "".join(ans)


class Solution3:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        stack = []
        res = []
        minch = "a"
        for c in s:
            stack.append(c)
            cnt[c] -= 1
            while minch != "z" and cnt[minch] == 0:
                minch = chr(ord(minch) + 1)
            while stack and stack[-1] <= minch:
                res.append(stack.pop())
        return "".join(res)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["robotWithString"] * 3,
            "kwargs": [
                dict(s="zza"),
                dict(s="bac"),
                dict(s="bdda"),
            ],
            "expected": ["azz", "abc", "addb"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
