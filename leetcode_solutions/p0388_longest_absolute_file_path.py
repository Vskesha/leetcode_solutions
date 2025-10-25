import unittest


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        lens = []
        lines = input.splitlines()

        for line in lines:
            tabs = line.count("\t")
            len_line = len(line) - tabs + 1
            lens = lens[:tabs] + [len_line]
            if "." in line:
                max_len = max(max_len, sum(lens) - 1)

        return max_len


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_length_longest_path_1(self):
        print("Test lengthLongestPath 1... ", end="")
        self.assertEqual(
            self.sol.lengthLongestPath(
                input="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
            ),
            20,
        )
        print("OK")

    def test_length_longest_path_2(self):
        print("Test lengthLongestPath 2... ", end="")
        self.assertEqual(
            self.sol.lengthLongestPath(
                input="dir\n"
                "\tsubdir1\n"
                "\t\tfile1.ext\n"
                "\t\tsubsubdir1\n"
                "\tsubdir2\n"
                "\t\tsubsubdir2\n"
                "\t\t\tfile2.ext"
            ),
            32,
        )
        print("OK")

    def test_length_longest_path_3(self):
        print("Test lengthLongestPath 3... ", end="")
        self.assertEqual(
            self.sol.lengthLongestPath(input="a"),
            0,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
