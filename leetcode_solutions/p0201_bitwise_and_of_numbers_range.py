class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            shift += 1
            left >>= 1
            right >>= 1
        return left << shift


class Solution2:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left = bin(left)[2:].zfill(32)
        right = bin(right)[2:].zfill(32)

        ans = ""
        for a, b in zip(left, right):
            if a == b:
                ans += a
            else:
                break

        ans += "0" * (32 - len(ans))
        return int(ans, 2)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.rangeBitwiseAnd(left=5, right=7) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.rangeBitwiseAnd(left=0, right=0) == 0
    print("OK")

    print("Test 3... ", end="")
    assert sol.rangeBitwiseAnd(left=1, right=2147483647) == 0
    print("OK")


if __name__ == "__main__":
    test()
