import unittest


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        while n or k:
            n, a = divmod(n, 2)
            k, b = divmod(k, 2)
            if a == 1 and b == 0:
                ans += 1
            elif a == 0 and b == 1:
                return -1
        return ans


class Solution2:
    def minChanges(self, n: int, k: int) -> int:
        n, k = bin(n)[2:], bin(k)[2:]
        if len(n) > len(k):
            k = k.zfill(len(n))
        else:
            n = n.zfill(len(k))
        ans = 0
        for a, b in zip(n, k):
            if a == "1" and b == "0":
                ans += 1
            elif a == "0" and b == "1":
                return -1
        return ans


class Solution3:
    def minChanges(self, n: int, k: int) -> int:
        n, k = bin(n)[2:], bin(k)[2:]
        ml = max(len(n), len(k))
        n, k = n.zfill(ml), k.zfill(ml)
        ans = 0
        for a, b in zip(n, k):
            if a == "1" and b == "0":
                ans += 1
            elif a == "0" and b == "1":
                return -1
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minChanges_1(self):
        print("Test minChanges 1... ", end="")
        self.assertEqual(2, self.sol.minChanges(n=13, k=4))
        print("OK")

    def test_minChanges_2(self):
        print("Test minChanges 2... ", end="")
        self.assertEqual(0, self.sol.minChanges(n=21, k=21))
        print("OK")

    def test_minChanges_3(self):
        print("Test minChanges 3... ", end="")
        self.assertEqual(-1, self.sol.minChanges(n=14, k=13))
        print("OK")


if __name__ == "__main__":
    unittest.main()
