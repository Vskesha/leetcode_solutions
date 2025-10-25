class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1


class Solution2:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            ans += n // 2
            n = (n + 1) // 2
        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.numberOfMatches(n=7) == 6
    print("OK")

    print("Test 2... ", end="")
    assert sol.numberOfMatches(n=14) == 13
    print("OK")


if __name__ == "__main__":
    test()
