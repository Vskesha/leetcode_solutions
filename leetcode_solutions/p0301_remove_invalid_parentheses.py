from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid(ss):
            op = 0
            for ch in ss:
                if ch == "(":
                    op += 1
                elif ch == ")":
                    if not op:
                        return False
                    op -= 1
            return op == 0

        op = td = 0
        ls = len(s)

        for ch in s:
            if ch == "(":
                op += 1
            elif ch == ")":
                if op:
                    op -= 1
                else:
                    td += 1
        td += op
        lss = ls - td

        def choose(pref, i, td) -> set[str]:
            if len(pref) == lss:
                return {pref} if is_valid(pref) else set()
            if not td:
                pref += s[i:]
                return {pref} if is_valid(pref) else set()
            if s[i].isalpha():
                return choose(pref + s[i], i + 1, td)
            return choose(pref + s[i], i + 1, td) | choose(pref, i + 1, td - 1)

        return list(choose("", 0, td))


class Solution2:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def remove(t, res, last_i, last_j, openParam, closeParam):
            balance = 0
            for i in range(last_i, len(t)):
                if t[i] == openParam:
                    balance += 1
                if t[i] == closeParam:
                    balance -= 1
                if balance >= 0:
                    continue

                for j in range(last_j, i + 1):
                    if t[j] == closeParam and (
                        j == last_j or t[j - 1] != closeParam
                    ):
                        remove(
                            t[0:j] + t[j + 1 : len(t)],
                            res,
                            i,
                            j,
                            openParam,
                            closeParam,
                        )
                return

            reversed_t = t[::-1]
            if openParam == "(":
                remove(reversed_t, res, 0, 0, closeParam, openParam)
            else:
                res.append(reversed_t)

        res = []
        openParam, closeParam = "(", ")"

        remove(s, res, 0, 0, openParam, closeParam)
        return res


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.removeInvalidParentheses(s="()())()") == ["(())()", "()()()"]
    print("OK")

    print("Test 2... ", end="")
    assert sol.removeInvalidParentheses(s="(a)())()") == ["(a())()", "(a)()()"]
    print("OK")

    print("Test 3... ", end="")
    assert sol.removeInvalidParentheses(s=")(") == [""]
    print("OK")


if __name__ == "__main__":
    test()
