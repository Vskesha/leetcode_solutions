class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i, d in enumerate(reversed(num)):
            if ord(d) % 2:
                return num[: len(num) - i]
        return ""


class Solution1:
    def largestOddNumber(self, num: str) -> str:
        odd = "13579"
        for i in range(len(num) - 1, -1, -1):
            if num[i] in odd:
                return num[: i + 1]
        return ""


class Solution2:
    def largestOddNumber(self, num: str) -> str:
        odd = "13579"
        for i, d in enumerate(reversed(num)):
            if d in odd:
                return num[: len(num) - i]
        return ""


class Solution3:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if ord(num[i]) % 2:
                return num[: i + 1]
        return ""


class Solution4:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2:
                return num[: i + 1]
        return ""


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.largestOddNumber(num="52") == "5"
    print("OK")

    print("Test 2... ", end="")
    assert sol.largestOddNumber(num="4206") == ""
    print("OK")

    print("Test 3... ", end="")
    assert sol.largestOddNumber(num="35427") == "35427"
    print("OK")


if __name__ == "__main__":
    test()
