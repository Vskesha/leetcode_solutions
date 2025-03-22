import unittest


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        if y > x:
            x, y = y, x
        while x or y:
            res += x % 2 != y % 2
            x, y = x // 2, y // 2
        return res


class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x or y:
            res += x % 2 != y % 2
            x, y = x // 2, y // 2
        return res


class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        bx, by = bin(x)[2:], bin(y)[2:]
        if x > y:
            by = by.zfill(len(bx))
        else:
            bx = bx.zfill(len(by))

        return sum(1 for a, b in zip(bx, by) if a != b)


class Solution3:
    def hammingDistance(self, x: int, y: int) -> int:
        xs = f"{x:b}"
        ys = f"{y:b}"
        if x > y:
            ys = ys.zfill(len(xs))
        else:
            xs = xs.zfill(len(ys))
        res = 0
        for i in range(len(xs)):
            if xs[i] != ys[i]:
                res += 1
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_hamming_distance_1(self):
        print("Test hammingDistance 1... ", end="")
        self.assertEqual(self.sol.hammingDistance(x=1, y=4), 2)
        print("OK")

    def test_hamming_distance_2(self):
        print("Test hammingDistance 2... ", end="")
        self.assertEqual(self.sol.hammingDistance(x=3, y=1), 1)
        print("OK")


if __name__ == "__main__":
    unittest.main()
