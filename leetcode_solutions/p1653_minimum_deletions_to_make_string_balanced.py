import unittest
from itertools import accumulate


class Solution:
    def minimumDeletions(self, s):
        ans, count = 0, 0
        for i in s:
            if i == "b":
                count += 1
            elif count:
                ans += 1
                count -= 1
        return ans


class Solution0:
    def minimumDeletions(self, s: str) -> int:
        acca = list(accumulate(1 if c == "a" else 0 for c in s))
        return min(0, min(i + 1 - ca * 2 for i, ca in enumerate(acca))) + acca[-1]


class Solution1:
    def minimumDeletions(self, s: str) -> int:
        ans = ca = 0
        for i, c in enumerate(s):
            if c == "a":
                ca += 1
            ans = min(ans, i + 1 - ca * 2)
        return ans + ca


class Solution2:
    def minimumDeletions(self, s: str) -> int:
        ans = ca = cb = 0

        for c in s:
            if c == "a":
                ca += 1
            else:
                cb += 1
            ans = min(ans, cb - ca)

        return ans + ca


class Solution3:
    def minimumDeletions(self, s: str) -> int:
        ans = ca = s.count("a")
        cb = 0

        for i, ch in enumerate(s):
            if ch == "a":
                ca -= 1
            else:
                cb += 1
            ans = min(ans, ca + cb)

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minimumDeletions_1(self):
        print("Test minimumDeletions 1... ", end="")
        self.assertEqual(2, self.sol.minimumDeletions(s="aababbab"))
        print("OK")

    def test_minimumDeletions_2(self):
        print("Test minimumDeletions 2... ", end="")
        self.assertEqual(2, self.sol.minimumDeletions(s="bbaaaaabb"))
        print("OK")


if __name__ == "__main__":
    unittest.main()
