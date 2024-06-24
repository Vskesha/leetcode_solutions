import unittest


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for ch in columnTitle:
            num = num * 26 + ord(ch) - 64
        return num


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_title_to_number_1(self):
        print("Test titleToNumber 1... ", end="")
        self.assertEqual(self.sol.titleToNumber(columnTitle="A"), 1)
        print("OK")

    def test_title_to_number_2(self):
        print("Test titleToNumber 2... ", end="")
        self.assertEqual(self.sol.titleToNumber(columnTitle="AB"), 28)
        print("OK")

    def test_title_to_number_3(self):
        print("Test titleToNumber 3... ", end="")
        self.assertEqual(self.sol.titleToNumber(columnTitle="ZY"), 701)
        print("OK")


if __name__ == "__main__":
    unittest.main()
