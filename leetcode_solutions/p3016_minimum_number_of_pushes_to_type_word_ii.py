import unittest
from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(
            mc[1] * (i // 8) for i, mc in enumerate(Counter(word).most_common(), 8)
        )


class Solution1:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        mc = Counter(word).most_common()
        for i, (_, fr) in enumerate(mc, 8):
            ans += i // 8 * fr
        return ans


class Solution2:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        fr = sorted(Counter(word).values(), reverse=True)
        ppl = 1
        for i in range(0, len(fr), 8):
            ans += sum(fr[i : i + 8]) * ppl
            ppl += 1
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_minimumPushes_1(self):
        print("Test minimumPushes 1... ", end="")
        self.assertEqual(self.sol.minimumPushes(word="abcde"), 5)
        print("OK")

    def test_minimumPushes_2(self):
        print("Test minimumPushes 2... ", end="")
        self.assertEqual(self.sol.minimumPushes(word="xyzxyzxyzxyz"), 12)
        print("OK")

    def test_minimumPushes_3(self):
        print("Test minimumPushes 3... ", end="")
        self.assertEqual(self.sol.minimumPushes(word="aabbccddeeffgghhiiiiii"), 24)
        print("OK")


if __name__ == "__main__":
    unittest.main()
