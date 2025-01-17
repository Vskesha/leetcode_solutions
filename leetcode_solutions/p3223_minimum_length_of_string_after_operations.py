import unittest
from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        return sum((q - 1) % 2 + 1 for q in Counter(s).values())


class Solution1:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        return 2 * len(cnt) - sum(c % 2 for c in cnt.values())


class Solution2:
    def minimumLength(self, s: str) -> int:
        ans = 0
        for q in Counter(s).values():
            ans += 1 if q % 2 else 2
        return ans


class Solution3:
    def minimumLength(self, s: str) -> int:
        ans = 0
        cnt = Counter(s)
        for c in cnt.values():
            ans += 2 - c % 2
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minimumLength_1(self):
        print("Test minimumLength 1... ", end="")
        self.assertEqual(5, self.sol.minimumLength(s="abaacbcbb"))
        print("OK")

    def test_minimumLength_2(self):
        print("Test minimumLength 2... ", end="")
        self.assertEqual(2, self.sol.minimumLength(s="aa"))
        print("OK")


if __name__ == "__main__":
    unittest.main()
