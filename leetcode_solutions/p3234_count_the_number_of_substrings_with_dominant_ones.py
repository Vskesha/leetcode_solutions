import unittest
from bisect import bisect_left
from itertools import accumulate


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        sacc = list(accumulate([1 if c == "0" else 0 for c in s], initial=0))
        ls = len(s)

        ans = 0
        for beg in range(ls):
            end = beg + 1
            while end <= ls:
                zeros = sacc[end] - sacc[beg]
                blocked_to = beg + zeros * (zeros + 1)
                if blocked_to <= end:
                    next_zero = bisect_left(sacc, sacc[beg] + zeros + 1)
                    ans += next_zero - end
                    end = next_zero
                else:
                    end = blocked_to

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_numberOfSubstrings_1(self):
        print("Test numberOfSubstrings 1... ", end="")
        self.assertEqual(5, self.sol.numberOfSubstrings(s="00011"))
        print("OK")

    def test_numberOfSubstrings_2(self):
        print("Test numberOfSubstrings 2... ", end="")
        self.assertEqual(16, self.sol.numberOfSubstrings(s="101101"))
        print("OK")


if __name__ == "__main__":
    unittest.main()
