from bisect import bisect_left
from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        indices = defaultdict(list)
        for i, ch in enumerate(s):
            indices[ch].append(i)
        ans = 0
        vals = list(indices.values())
        for ids1 in vals:
            if len(ids1) < 2:
                continue
            fo, lo = ids1[0] + 1, ids1[-1]
            for ids2 in vals:
                i = bisect_left(ids2, fo)
                if i < len(ids2) and ids2[i] < lo:
                    ans += 1
        return ans


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.countPalindromicSubsequence(s="aabca") == 3
    print('OK')

    print('Test 2 ... ', end='')
    assert sol.countPalindromicSubsequence(s="adc") == 0
    print('OK')

    print('Test 3 ... ', end='')
    assert sol.countPalindromicSubsequence(s="bbcbaba") == 4
    print('OK')


if __name__ == '__main__':
    test()
