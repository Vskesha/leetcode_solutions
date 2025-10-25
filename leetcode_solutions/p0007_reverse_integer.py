class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = int(str(-x if negative else x)[::-1])
        if negative:
            x = -x
            if x < -(2**31):
                return 0
            return x
        if x > 2**31 - 1:
            return 0
        return x


class Solution1:
    def reverse(self, x: int) -> int:
        negative = x < 0
        if negative:
            x = -x
        x = int(str(x)[::-1])
        if negative:
            x = -x
            if x < -(2**31):
                return 0
        if x > 2**31 - 1:
            return 0
        return x


class Solution2:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0].isnumeric():
            x = int(s[::-1])
        else:
            x = int(s[0] + s[1:][::-1])
        if abs(x) > 2**31 - 1:
            return 0
        return x


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.reverse(x=123) == 321
    print("OK")

    print("Test 2... ", end="")
    assert sol.reverse(x=-123) == -321
    print("OK")

    print("Test 3... ", end="")
    assert sol.reverse(x=120) == 21
    print("OK")


if __name__ == "__main__":
    test()
