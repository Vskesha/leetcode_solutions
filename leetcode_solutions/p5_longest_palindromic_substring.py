class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = len(s)
        max_len = 0
        start, stop = 0, 0
        for i in range(ls):
            for d in range(2):
                b, e = i, i + d
                while b >= 0 and e < ls and s[b] == s[e]:
                    b -= 1
                    e += 1
                b += 1
                if max_len < e - b:
                    max_len = e - b
                    start, stop = b, e

        return s[start:stop]


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.longestPalindrome(s="babad") == 'bab'
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.longestPalindrome(s="cbbd") == 'bb'
    print('ok')


if __name__ == '__main__':
    test()
