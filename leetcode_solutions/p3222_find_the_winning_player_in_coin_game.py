import unittest


class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        moves = min(x, y // 4)
        return "Alice" if moves % 2 else "Bob"


class Solution2:
    def losingPlayer(self, x: int, y: int) -> str:
        alice = False

        while x and y > 3:
            x -= 1
            y -= 4
            alice = not alice

        return "Alice" if alice else "Bob"


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_losingPlayer_1(self):
        print("Test losingPlayer 1... ", end="")
        self.assertEqual("Alice", self.sol.losingPlayer(x=2, y=7))
        print("OK")

    def test_losingPlayer_2(self):
        print("Test losingPlayer 2... ", end="")
        self.assertEqual("Bob", self.sol.losingPlayer(x=4, y=11))
        print("OK")


if __name__ == "__main__":
    unittest.main()
