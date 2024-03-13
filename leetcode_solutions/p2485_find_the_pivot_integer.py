import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        x = math.sqrt(n * (n + 1) / 2)
        return int(x) if int(x) == x else -1


class Solution2:
    def pivotInteger(self, n: int) -> int:
        x = int((n * (n + 1) // 2) ** 0.5)
        return x if x * (x - 1) == (n - x) * (n + x + 1) else -1


def test_pivot_integer():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.pivotInteger(n=8) == 6
    print("OK")

    print("Test 2... ", end="")
    assert sol.pivotInteger(n=1) == 1
    print("OK")

    print("Test 3... ", end="")
    assert sol.pivotInteger(n=4) == -1
    print("OK")


if __name__ == "__main__":
    test_pivot_integer()
