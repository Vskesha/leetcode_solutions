import unittest
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(s[11:13]) > 60 for s in details)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_countSeniors_1(self):
        print("Test countSeniors 1... ", end="")
        self.assertEqual(
            2,
            self.sol.countSeniors(
                details=[
                    "7868190130M7522",
                    "5303914400F9211",
                    "9273338290F4010",
                ]
            ),
        )
        print("OK")

    def test_countSeniors_2(self):
        print("Test countSeniors 2... ", end="")
        self.assertEqual(
            0,
            self.sol.countSeniors(
                details=["1313579440F2036", "2921522980M5644"]
            ),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
