from typing import List


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []

        for i in range(len(s)):
            ch = s[i]
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""

        for i in stack:
            s[i] = ""

        return "".join(s)


class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack: List[int] = []
        result: List[str] = []
        for c in s:
            if c == "(":
                stack.append(len(result))
                result.append(c)
            elif c == ")":
                if stack:
                    stack.pop()
                    result.append(c)
            else:
                result.append(c)

        for i in stack:
            result[i] = ""

        return "".join(result)


class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        aux = []
        op = 0
        for ch in s:
            if ch == "(":
                op += 1
            if ch == ")":
                op -= 1
            if op >= 0:
                aux.append(ch)
            else:
                op = 0
        if op == 0:
            return "".join(aux)
        op = 0
        ans = []
        for ch in reversed(aux):
            if ch == ")":
                op += 1
            if ch == "(":
                op -= 1
            if op >= 0:
                ans.append(ch)
            else:
                op = 0

        return "".join(reversed(ans))


def is_valid_parentheses(s: str) -> bool:
    op = 0
    for ch in s:
        if ch == "(":
            op += 1
        elif ch == ")":
            op -= 1
            if op < 0:
                return False
    return op == 0


def test_min_remove_to_make_valid():
    sol = Solution()

    print("Test 1... ", end="")
    assert is_valid_parentheses(sol.minRemoveToMakeValid(s="lee(t(c)o)de)"))
    print("OK")

    print("Test 2... ", end="")
    assert is_valid_parentheses(sol.minRemoveToMakeValid(s="a)b(c)d"))
    print("OK")

    print("Test 3... ", end="")
    assert is_valid_parentheses(sol.minRemoveToMakeValid(s="))(("))
    print("OK")

    print("Test 4... ", end="")
    assert is_valid_parentheses(sol.minRemoveToMakeValid(s="(a(b(c)d)"))
    print("OK")


if __name__ == "__main__":
    test_min_remove_to_make_valid()
