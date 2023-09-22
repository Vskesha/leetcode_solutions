class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return True if i == len(s) else False


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.isSubsequence(s="abc", t="ahbgdc") is True
    print('ok\nTest 2 ... ', end='')
    assert sol.isSubsequence(s="axc", t="ahbgdc") is False
    print('ok')


if __name__ == '__main__':
    test()
