import unittest
from collections import Counter, OrderedDict
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = OrderedDict()

        for s in arr:
            cnt[s] = cnt.get(s, 0) + 1

        for s, fr in cnt.items():
            if fr == 1:
                if k == 1:
                    return s
                k -= 1

        return ""


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        for s in arr:
            if cnt[s] == 1:
                k -= 1
                if not k:
                    return s
        return ""


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_kthDistinct_1(self):
        print("Test kthDistinct 1... ", end="")
        self.assertEqual(
            "a", self.sol.kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2)
        )
        print("OK")

    def test_kthDistinct_2(self):
        print("Test kthDistinct 2... ", end="")
        self.assertEqual(
            "aaa", self.sol.kthDistinct(arr=["aaa", "aa", "a"], k=1)
        )
        print("OK")

    def test_kthDistinct_3(self):
        print("Test kthDistinct 3... ", end="")
        self.assertEqual("", self.sol.kthDistinct(arr=["a", "b", "a"], k=3))
        print("OK")


if __name__ == "__main__":
    unittest.main()
