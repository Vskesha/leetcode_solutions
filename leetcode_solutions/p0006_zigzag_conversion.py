import unittest
from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        rows = [[] for _ in range(numRows)]
        i, direction = 0, 1
        for char in s:
            rows[i].append(char)
            i += direction
            if i == 0 or i == numRows - 1:
                direction *= -1
        return "".join("".join(row) for row in rows)


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        k = (numRows - 1) * 2
        sl: List = list(s)
        d = -len(s) % k
        sl.extend([""] * d)
        ls = len(s)
        ans = sl[::k]
        for i in range(1, k // 2):
            for j in range(0, ls, k):
                ans.append(s[j + i])
                ans.append(s[j + k - i])
        ans.extend(s[k // 2 :: k])
        return "".join(ans)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_convert_1(self):
        print("Test convert 1... ", end="")
        self.assertEqual(
            self.sol.convert(s="PAYPALISHIRING", numRows=3), "PAHNAPLSIIGYIR"
        )
        print("OK")

    def test_convert_2(self):
        print("Test convert 2... ", end="")
        self.assertEqual(
            self.sol.convert(s="PAYPALISHIRING", numRows=4), "PINALSIGYAHRPI"
        )
        print("OK")

    def test_convert_3(self):
        print("Test convert 3... ", end="")
        self.assertEqual(self.sol.convert(s="A", numRows=1), "A")
        print("OK")


if __name__ == "__main__":
    unittest.main()
