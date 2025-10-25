from typing import List


class Solution:
    def validateStackSequences(
        self, pushed: List[int], popped: List[int]
    ) -> bool:
        stack = []
        i = 0
        for n in popped:
            if n in stack:
                if stack[-1] == n:
                    stack.pop()
                    continue
                else:
                    return False
            while pushed[i] != n:
                stack.append(pushed[i])
                i += 1
            i += 1
        return True


class Solution1:
    def validateStackSequences(
        self, pushed: List[int], popped: List[int]
    ) -> bool:
        stack = []
        lp = len(pushed)
        i = 0
        for n in popped:
            if stack and stack[-1] == n:
                stack.pop()
                continue
            if i >= lp:
                return False
            while i < lp and pushed[i] != n:
                stack.append(pushed[i])
                i += 1
            i += 1
        return True


class Solution2:
    def validateStackSequences(
        self, pushed: List[int], popped: List[int]
    ) -> bool:
        stack = []
        lp = len(pushed)
        i = j = 0
        while i <= lp:
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            while i < lp and pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1
            i += 1
            j += 1
        return not stack


class Solution3:
    def validateStackSequences(
        self, pushed: List[int], popped: List[int]
    ) -> bool:
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return stack == []


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.validateStackSequences(
            pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]
        )
        is True
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.validateStackSequences(
            pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]
        )
        is False
    )
    print("OK")


if __name__ == "__main__":
    test()
