class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        ln = n = 0
        s = s.replace(" ", "") + " "
        op = "+"

        for ch in s:
            if ch.isnumeric():
                n = n * 10 + int(ch)
            else:
                if op == "*":
                    ln *= n
                elif op == "/":
                    ln = int(ln / n)
                else:
                    res += ln
                    ln = n if op == "+" else -n
                op = ch
                n = 0

        return res + ln


class Solution2:
    def calculate(self, s: str) -> int:
        stack = ["+"]
        n = 0
        s = s.replace(" ", "") + " "

        for ch in s:
            if ch.isdigit():
                n = n * 10 + int(ch)
            else:
                if stack and stack[-1] in "/*":
                    operator = stack.pop()
                    stack[-1] = (
                        stack[-1] * n if operator == "*" else stack[-1] // n
                    )
                else:
                    stack.append(n)
                stack.append(ch)
                n = 0
        stack.pop()
        for i in range(0, len(stack), 2):
            if stack[i] == "+":
                n += stack[i + 1]
            else:
                n -= stack[i + 1]

        return n


def test_calculate():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.calculate(s="3+2*2") == 7
    print("OK")

    print("Test 2... ", end="")
    assert sol.calculate(s=" 3/2 ") == 1
    print("OK")

    print("Test 3... ", end="")
    assert sol.calculate(s=" 3+5 / 2 ") == 5
    print("OK")


if __name__ == "__main__":
    test_calculate()
