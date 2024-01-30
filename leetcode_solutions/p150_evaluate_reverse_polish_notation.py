from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == "+":
                x = st.pop()
                st[-1] += x
            elif t == "-":
                x = st.pop()
                st[-1] -= x
            elif t == "*":
                x = st.pop()
                st[-1] *= x
            elif t == "/":
                x = st.pop()
                sign = (st[-1] < 0) ^ (x < 0)
                st[-1] = abs(st[-1]) // abs(x)
                if sign:
                    st[-1] *= -1
            else:
                st.append(int(t))

        return st[-1]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.evalRPN(tokens=["2", "1", "+", "3", "*"]) == 9
    print("OK")

    print("Test 2... ", end="")
    assert sol.evalRPN(tokens=["4", "13", "5", "/", "+"]) == 6
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.evalRPN(
            tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
        == 22
    )
    print("OK")


if __name__ == "__main__":
    test()
