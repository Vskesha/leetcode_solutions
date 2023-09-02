class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1


def main():
    sol = Solution()
    print('Test 1 ... ', end='')
    s = ["h", "e", "l", "l", "o"]
    sol.reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]
    print('ok')
    print('Test 2 ... ', end='')
    s = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
    print('ok')


if __name__ == '__main__':
    main()
