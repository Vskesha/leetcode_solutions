from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        st = 0
        ans = []
        prev = s[0]

        for i, ch in enumerate(s):
            if ch != prev:
                if i - st > 2:
                    ans.append([st, i - 1])
                st = i
            prev = ch
        if len(s) - st > 2:
            ans.append([st, len(s) - 1])
        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.largeGroupPositions(s="abbxxxxzzy") == [[3, 6]]
    print('OK')

    print('Test 2... ', end='')
    assert sol.largeGroupPositions(s="abc") == []
    print('OK')

    print('Test 3... ', end='')
    assert sol.largeGroupPositions(s="abcdddeeeeaabbbcd") == [[3, 5], [6, 9], [12, 14]]
    print('OK')


if __name__ == '__main__':
    test()
