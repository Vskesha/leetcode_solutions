class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


class Solution2:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1].lower() == ch.lower() and stack[-1] != ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


def test_make_good():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.makeGood(s="leEeetcode") == "leetcode"
    print("OK")

    print("Test 2... ", end="")
    assert sol.makeGood(s="abBAcC") == ""
    print("OK")


if __name__ == "__main__":
    test_make_good()
