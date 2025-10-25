from itertools import cycle


class Solution:
    def minOperations(self, s: str) -> int:
        return min(
            d := sum(s[i] == str(i % 2) for i in range(len(s))), len(s) - d
        )


class Solution2:
    def minOperations(self, s: str) -> int:
        return min(
            d := sum(a == b for a, b in zip(s, cycle("01"))), len(s) - d
        )


class Solution3:
    def minOperations(self, s: str) -> int:
        d = sum(c == str(i % 2) for i, c in enumerate(s))
        return min(d, len(s) - d)


class Solution4:
    def minOperations(self, s: str) -> int:
        d = 0
        for i, c in enumerate(s):
            d += c == str(i % 2)
        return min(d, len(s) - d)


class Solution5:
    def minOperations(self, s: str) -> int:
        d1 = d2 = 0
        for i, c in enumerate(s):
            if c == str(i % 2):
                d1 += 1
            else:
                d2 += 1
        return min(d1, d2)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.minOperations(s="0100") == 1
    print("OK")

    print("Test 2... ", end="")
    assert sol.minOperations(s="10") == 0
    print("OK")

    print("Test 3... ", end="")
    assert sol.minOperations(s="1111") == 2
    print("OK")


if __name__ == "__main__":
    test()
