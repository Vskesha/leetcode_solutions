from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
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
    assert sol.smallestSubsequence(s="bcabc") == "abc"
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.smallestSubsequence(s="cbacdcbc") == "acdb"
    print("OK")

    print("Test 3 ... ", end="")
    assert sol.smallestSubsequence(s="abacb") == "abc"
    print("OK")


if __name__ == "__main__":
    test()
