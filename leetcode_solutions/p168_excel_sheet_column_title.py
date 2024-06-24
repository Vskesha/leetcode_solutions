import unittest


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber, rem = divmod(columnNumber - 1, 26)
            res.append(chr(rem + 65))
        return "".join(res[::-1])


class Solution2:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            res = (chr((columnNumber - 1) % 26 + 65)) + res
            columnNumber = (columnNumber - 1) // 26
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_convert_to_title_1(self):
        print("Test convertToTitle 1... ", end="")
        self.assertEqual(self.sol.convertToTitle(columnNumber=1), "A")
        print("OK")

    def test_convert_to_title_2(self):
        print("Test convertToTitle 2... ", end="")
        self.assertEqual(self.sol.convertToTitle(columnNumber=28), "AB")
        print("OK")

    def test_convert_to_title_3(self):
        print("Test convertToTitle 3... ", end="")
        self.assertEqual(self.sol.convertToTitle(columnNumber=701), "ZY")
        print("OK")


if __name__ == "__main__":
    unittest.main()
