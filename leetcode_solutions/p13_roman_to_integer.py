class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = 2000
        ans = 0
        for ch in s:
            n = table[ch]
            if prev < n:
                ans -= prev * 2
            ans += n
            prev = n
        return ans


class Solution2:
    def romanToInt(self, s: str) -> int:
        trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = ans = 0
        for i in range(len(s) - 1, -1, -1):
            ans += -trans[s[i]] if trans[s[i]] < prev else trans[s[i]]
            prev = trans[s[i]]
        return ans


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.romanToInt(s="III") == 3
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.romanToInt(s="LVIII") == 58
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.romanToInt(s="MCMXCIV") == 1994
    print('ok')


if __name__ == '__main__':
    test()
