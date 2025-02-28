import unittest


class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        for el in path.split("/"):
            if el and el != "." and el != "..":
                result.append(el)
            if el == ".." and result:
                result.pop()
        return "/" + "/".join(result)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_simplify_path_1(self):
        print("Test simplifyPath 1... ", end="")
        self.assertEqual(self.sol.simplifyPath(path="/home/"), "/home")
        print("OK")

    def test_simplify_path_2(self):
        print("Test simplifyPath 2... ", end="")
        self.assertEqual(self.sol.simplifyPath(path="/home//foo/"), "/home/foo")
        print("OK")

    def test_simplify_path_3(self):
        print("Test simplifyPath 3... ", end="")
        self.assertEqual(
            self.sol.simplifyPath(path="/home/user/Documents/../Pictures"),
            "/home/user/Pictures",
        )
        print("OK")

    def test_simplify_path_4(self):
        print("Test simplifyPath 4... ", end="")
        self.assertEqual(self.sol.simplifyPath(path="/../"), "/")
        print("OK")

    def test_simplify_path_5(self):
        print("Test simplifyPath 5... ", end="")
        self.assertEqual(
            self.sol.simplifyPath(path="/.../a/../b/c/../d/./"), "/.../b/d"
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
