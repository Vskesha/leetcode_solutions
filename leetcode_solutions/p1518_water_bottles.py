import unittest


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = empty = 0
        while numBottles:
            ans += numBottles
            numBottles, empty = divmod(numBottles + empty, numExchange)
        return ans


class Solution2:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = empty = 0
        while numBottles:
            ans += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_num_water_bottles_1(self):
        print("Test numWaterBottles 1... ", end="")
        self.assertEqual(self.sol.numWaterBottles(numBottles=9, numExchange=3), 13)
        print("OK")

    def test_num_water_bottles_2(self):
        print("Test numWaterBottles 2... ", end="")
        self.assertEqual(self.sol.numWaterBottles(numBottles=15, numExchange=4), 19)
        print("OK")


if __name__ == "__main__":
    unittest.main()
