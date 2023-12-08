from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = {ch: i for i, ch in enumerate(s)}
        lo, prev = 0, -1
        ans = []
        for i, ch in enumerate(s):
            lo = max(lo, last_occ[ch])
            if i == lo:
                ans.append(i - prev)
                prev = i
        return ans


class Solution1:
    def partitionLabels(self, s: str) -> List[int]:
        start, end = 0, 0
        i = 0
        ans = []
        while i < len(s):
            end = max(end, s.rindex(s[i]))
            if i == end:
                end += 1
                ans.append(end - start)
                start = end
            i += 1
        return ans


class Solution2:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = {}
        for i, ch in enumerate(s):
            last_occ[ch] = i

        lo = 0
        prev = 0
        ans = []
        for i, ch in enumerate(s):
            if i > lo:
                ans.append(i - prev)
                prev = i
            lo = max(lo, last_occ[ch])
        ans.append(len(s) - prev)
        return ans


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.partitionLabels(s="ababcbacadefegdehijhklij") == [9, 7, 8]
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.partitionLabels(s="eccbbbbdec") == [10]
    print('ok')


if __name__ == '__main__':
    test()
