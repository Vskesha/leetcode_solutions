from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []
        setex, curex = set(), {""}

        for c in expression:
            if c == "{":
                stack.append((setex, curex))
                setex, curex = set(), {""}

            elif c == "}":
                totex = setex.union(curex)
                setex, curex = stack.pop()
                curex = {s1 + s2 for s1 in curex for s2 in totex}

            elif c == ",":
                setex.update(curex)
                curex = {""}

            else:
                curex = {s1 + c for s1 in curex}

        return sorted(curex)


class Solution1:
    def braceExpansionII(self, expression: str) -> List[str]:
        def rec():
            nonlocal i
            res = set()
            if expression[i] == "{":
                i += 1
                res.update(rec())
                while i < le and expression[i] == ",":
                    i += 1
                    res.update(rec())
                i += 1
            elif expression[i].isalpha():
                w = ""
                while i < le and expression[i].isalpha():
                    w += expression[i]
                    i += 1
                res.add(w)
            if i < le and (expression[i] == "{" or expression[i].isalpha()):
                res = {a + b for b in rec() for a in res}
            return res

        i = 0
        le = len(expression)
        return sorted(rec())


class Solution2:
    def braceExpansionII(self, expression: str) -> List[str]:
        def getWord():
            nonlocal i
            word = ""
            while i < len(expression) and expression[i].isalpha():
                word += expression[i]
                i += 1
            return word

        def dfs():
            nonlocal i
            res = set()
            if expression[i] == "{":
                i += 1
                res.update(dfs())
                while i < len(expression) and expression[i] == ",":
                    i += 1
                    res.update(dfs())
                i += 1
            elif expression[i].isalpha():
                res.add(getWord())

            while i < len(expression) and (
                expression[i] == "{" or expression[i].isalpha()
            ):
                res = {w + a for a in dfs() for w in res}
            return res

        i = 0
        return sorted(dfs())


class Solution3:
    def braceExpansionII(self, expression: str) -> List[str]:
        def divis(exp):
            # delete first { and last } if 'exp' surrended with {}
            if exp[0] == "{" and exp[-1] == "}":
                closed = 0
                for i, c in enumerate(exp):
                    if c == "{":
                        closed += 1
                    elif c == "}":
                        closed -= 1
                    if not closed:
                        closed = i
                        break
                if closed == len(exp) - 1:
                    exp = exp[1:-1]

            # if no brackets in 'exp' return splitted by comma set
            if "{" not in exp:
                return set(exp.split(","))

            # divide 'exp' on two parts that was separated with comma
            # and return their joined set
            left, right = "", ""
            brackets = 0
            for i, c in enumerate(exp):
                if c == "{":
                    brackets += 1
                elif c == "}":
                    brackets -= 1
                elif c == "," and brackets == 0:
                    left = exp[:i]
                    right = exp[i + 1 :]
                    break
            if left:
                l_set = divis(left)
                r_set = divis(right)
                return l_set | r_set

            # divide 'exp' on two parts and return their product
            if exp[0] == "{":
                i = 0
                for j, c in enumerate(exp):
                    if c == "{":
                        i += 1
                    elif c == "}":
                        i -= 1
                    if not i:
                        i = j + 1
            else:
                i = exp.index("{")
            left = exp[:i]
            right = exp[i:]
            l_set = divis(left)
            r_set = divis(right)
            return {a + b for a in l_set for b in r_set}

        return sorted(list(divis(expression)))


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.braceExpansionII("{a,b}{c,{d,e}}") == [
        "ac",
        "ad",
        "ae",
        "bc",
        "bd",
        "be",
    ]
    print("ok\nTest 2 ... ", end="")
    assert sol.braceExpansionII("{{a,z},a{b,c},{ab,z}}") == [
        "a",
        "ab",
        "ac",
        "z",
    ]
    print("ok\nTest 3 ... ", end="")
    assert sol.braceExpansionII("n{g,{u,o}}{a,{x,ia,o},w}") == [
        "nga",
        "ngia",
        "ngo",
        "ngw",
        "ngx",
        "noa",
        "noia",
        "noo",
        "now",
        "nox",
        "nua",
        "nuia",
        "nuo",
        "nuw",
        "nux",
    ]
    print("ok")


if __name__ == "__main__":
    test()
