from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remain = Counter(s)
        stack = []
        seen = set()

        for ch in s:
            remain[ch] -= 1
            if ch in seen:
                continue
            while stack and stack[-1] > ch and remain[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)

        return "".join(stack)


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.removeDuplicateLetters(s="bcabc") == "abc"
    print("ok\nTest 2 ... ", end="")
    assert sol.removeDuplicateLetters(s="cbacdcbc") == "acdb"
    print("ok\nTest 3 ... ", end="")
    assert sol.removeDuplicateLetters(s="abacb") == "abc"
    print("ok")


if __name__ == "__main__":
    test()
