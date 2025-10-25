import unittest
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        d = 0
        for log in logs:
            if log == "../":
                if d:
                    d -= 1
            elif log != "./":
                d += 1
        return d


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_operations_1(self):
        print("Test minOperations 1... ", end="")
        self.assertEqual(
            self.sol.minOperations(logs=["d1/", "d2/", "../", "d21/", "./"]), 2
        )
        print("OK")

    def test_min_operations_2(self):
        print("Test minOperations 2... ", end="")
        self.assertEqual(
            self.sol.minOperations(
                logs=["d1/", "d2/", "./", "d3/", "../", "d31/"]
            ),
            3,
        )
        print("OK")

    def test_min_operations_3(self):
        print("Test minOperations 3... ", end="")
        self.assertEqual(
            self.sol.minOperations(logs=["d1/", "../", "../", "../"]), 0
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
