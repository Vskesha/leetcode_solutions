class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return (
            max(
                [
                    num[i]
                    for i in range(2, len(num))
                    if num[i] == num[i - 1] == num[i - 2]
                ]
                + [""]
            )
            * 3
        )


class Solution1:
    def largestGoodInteger(self, num: str) -> str:
        for i in reversed(range(10)):
            if str(i) * 3 in num:
                return str(i) * 3
        return ""


class Solution2:
    def largestGoodInteger(self, num: str) -> str:
        mv = "/"

        for i in range(2, len(num)):
            if num[i] == num[i - 1] == num[i - 2]:
                mv = max(mv, num[i])

        return "" if mv == "/" else mv * 3


class Solution3:
    def largestGoodInteger(self, num: str) -> str:
        a, b, c = "", num[0], num[1]
        mv = "/"

        for i in range(2, len(num)):
            a, b, c = b, c, num[i]
            if a == b == c:
                mv = max(mv, a)

        return "" if mv == "/" else mv * 3


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.largestGoodInteger(num="6777133339") == "777"
    print("OK")

    print("Test 2... ", end="")
    assert sol.largestGoodInteger(num="2300019") == "000"
    print("OK")

    print("Test 3... ", end="")
    assert sol.largestGoodInteger(num="42352338") == ""
    print("OK")


if __name__ == "__main__":
    test()
