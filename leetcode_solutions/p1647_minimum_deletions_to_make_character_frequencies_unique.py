from collections import Counter
from heapq import heappop, heapify


class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        mc = Counter(s).most_common()
        curr = mc[0][1]
        for _, val in mc:
            if val > curr:
                ans += val - curr
            else:
                curr = val
            if curr:
                curr -= 1

        return ans


class Solution2:
    def minDeletions(self, s: str) -> int:
        ans = 0
        vals = sorted(Counter(s).values(), reverse=True)
        curr = vals[0]
        for val in vals:
            if val > curr:
                ans += val - curr
            else:
                curr = val
            if curr:
                curr -= 1

        return ans


# Heap / Priority Queue Approach
class Solution3:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        deletions = 0
        used_frequencies = set()

        heap = list(cnt.values())
        heapify(heap)

        while heap:
            freq = heappop(heap)
            while freq > 0 and freq in used_frequencies:
                freq -= 1
                deletions += 1
            used_frequencies.add(freq)

        return deletions


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.minDeletions(s="aab") == 0
    print('ok')
    print('Test 2 ... ', end='')
    assert sol.minDeletions(s="aaabbbcc") == 2
    print('ok')
    print('Test 3 ... ', end='')
    assert sol.minDeletions(s="ceabaacb") == 2
    print('ok')


if __name__ == '__main__':
    test()
