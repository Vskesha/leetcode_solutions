from collections import deque


class Solution:
    def checkValidString(self, s: str) -> bool:
        opened = []
        asters = deque()

        for i, ch in enumerate(s):
            if ch == "(":
                opened.append(i)
            elif ch == "*":
                asters.append(i)
            elif opened:
                opened.pop()
            elif asters:
                asters.popleft()
            else:
                return False

        while opened and asters and opened[-1] < asters[-1]:
            opened.pop()
            asters.pop()

        return not opened


class Solution2:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0

        for c in s:
            if c == "(":
                lo, hi = lo + 1, hi + 1
            elif c == ")":
                lo, hi = lo - 1, hi - 1
            else:
                lo = lo - 1
                hi = hi + 1
            if hi < 0:
                return False
            if lo < 0:
                lo = 0
        return lo == 0


def test_check_valid_string():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.checkValidString(s="()") is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.checkValidString(s="(*)") is True
    print("OK")

    print("Test 3... ", end="")
    assert sol.checkValidString(s="(*))") is True
    print("OK")

    print("Test 4... ", end="")
    assert (
        sol.checkValidString(
            s="(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(("
            "))(()))())((*()()(((()((()*(())*(()**)()(())"
        )
        is False
    )
    print("OK")


if __name__ == "__main__":
    test_check_valid_string()
