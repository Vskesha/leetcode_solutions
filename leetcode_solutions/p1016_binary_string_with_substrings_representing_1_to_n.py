import unittest


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        return all(bin(t)[2:] in s for t in range(n, 0, -1))


class Solution2:
    def queryString(self, s: str, n: int) -> bool:
        for k in range(n, 0, -1):
            if bin(k)[2:] not in s:
                return False
        return True


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_query_string_1(self):
        print("Test queryString 1... ", end="")
        self.assertTrue(self.sol.queryString(s="0110", n=3))
        print("OK")

    def test_query_string_2(self):
        print("Test queryString 2... ", end="")
        self.assertFalse(self.sol.queryString(s="0110", n=4))
        print("OK")


if __name__ == "__main__":
    unittest.main()
