import unittest


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = int(c**0.5), 0
        while i >= j:
            ss = i * i + j * j
            if ss == c:
                return True
            elif ss < c:
                j += 1
            else:
                i -= 1
        return False


class Solution2:
    def judgeSquareSum(self, c: int) -> bool:
        i = 2
        while i * i <= c:
            cnt = 0
            while c % i == 0:
                c //= i
                cnt += 1
            if cnt % 2 == 1 and i % 4 == 3:
                return False
            i += 1
        return c % 4 != 3


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_judge_square_sum_1(self):
        print("Test judgeSquareSum 1... ", end="")
        self.assertTrue(self.sol.judgeSquareSum(c=5))
        print("OK")

    def test_judge_square_sum_2(self):
        print("Test judgeSquareSum 2... ", end="")
        self.assertFalse(self.sol.judgeSquareSum(c=3))
        print("OK")


if __name__ == "__main__":
    unittest.main()
