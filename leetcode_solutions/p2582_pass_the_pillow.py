import unittest


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        return (
            n - time % (n - 1) if time // (n - 1) % 2 else time % (n - 1) + 1
        )


class Solution2:
    def passThePillow(self, n: int, time: int) -> int:
        i = d = 1
        for _ in range(time):
            i += d
            if i == 1 or i == n:
                d *= -1
        return i


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_pass_the_pillow_1(self):
        print("Test passThePillow 1... ", end="")
        self.assertEqual(self.sol.passThePillow(n=4, time=5), 2)
        print("OK")

    def test_pass_the_pillow_2(self):
        print("Test passThePillow 2... ", end="")
        self.assertEqual(self.sol.passThePillow(n=3, time=2), 3)
        print("OK")


if __name__ == "__main__":
    unittest.main()
