from functools import lru_cache


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        for i, ch in enumerate(reversed(bin(n)), 1):
            if ch == "1":
                ans = 2**i - ans - 1
        return ans


class Solution1:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = unset = 0
        for ch in reversed(bin(n)):
            unset = unset * 2 + 1
            if ch == "1":
                ans = unset - ans
        return ans


class Solution2:
    def minimumOneBitOperations(self, n: int) -> int:
        ans, i = 0, 0
        unset = 1
        while n:
            if n % 2:
                ans = unset - ans
            unset = unset * 2 + 1
            n //= 2
            i += 1
        return ans


class Solution3:
    def minimumOneBitOperations(self, n: int) -> int:
        if not n:
            return 0

        @lru_cache(None)
        def unset_bit(i) -> int:
            """1...0100...0 -> 1...0110...0 -> 1...0010...0"""
            if not i:
                return 1
            return set_bit(i - 1) + unset_bit(i - 1) + 1

        @lru_cache(None)
        def set_bit(i) -> int:
            """1...0000...0 -> 1...0010...0 -> 1...0110...0 -> 1...0100...0"""
            if not i:
                return 1
            return set_bit(i - 1) + unset_bit(i - 1) + 1

        pos = [i for i, ch in enumerate(reversed(bin(n))) if ch == "1"]

        ans = 0
        for p in pos:
            ans = unset_bit(p) - ans
        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.minimumOneBitOperations(n=3) == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.minimumOneBitOperations(n=6) == 4
    print("OK")


if __name__ == "__main__":
    test()
