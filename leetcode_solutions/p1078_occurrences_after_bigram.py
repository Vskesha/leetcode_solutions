import unittest
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        txt = text.split()
        return [
            txt[i + 2]
            for i in range(len(txt) - 2)
            if txt[i] == first and txt[i + 1] == second
        ]


class Solution2:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        ans = []

        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                ans.append(words[i + 2])

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_find_occurrences_1(self):
        print("Test findOccurrences 1... ", end="")
        self.assertListEqual(
            self.sol.findOcurrences(
                text="alice is a good girl she is a good student",
                first="a",
                second="good",
            ),
            ["girl", "student"],
        )
        print("OK")

    def test_find_occurrences_2(self):
        print("Test findOccurrences 2... ", end="")
        self.assertListEqual(
            self.sol.findOcurrences(
                text="we will we will rock you", first="we", second="will"
            ),
            ["we", "rock"],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
