from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = 0
        for letters in zip(*strs):
            if len(set(letters)) == 1:
                ans += 1
            else:
                break
        return strs[0][:ans]


class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pr = strs[0]

        for s in strs:
            ml = min(len(pr), len(s))
            for i in range(ml):
                if pr[i] != s[i]:
                    pr = pr[:i]
                    break
            else:
                pr = pr[:ml]
        return pr


class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def char_in_all_strings(i: int) -> bool:
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return False
            return True

        min_len_str = min(strs, key=len)
        min_len = len(min_len_str)
        for i in range(min_len):
            if not char_in_all_strings(i):
                return strs[0][:i]

        return min_len_str


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    print('OK')

    print('Test 2... ', end='')
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == "racecar"
    print('OK')


if __name__ == '__main__':
    test()
