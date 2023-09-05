from collections import Counter, defaultdict
from itertools import permutations


class Solution:
    def largestVariance(self, s: str) -> int:

        result = 0
        count = defaultdict(int)
        index = defaultdict(list)
        for i, ch in enumerate(s):
            count[ch] += 1
            index[ch].append((i, ch))

        for a, b in permutations(count.keys(), 2):
            total, flag = 0, False
            if count[b] - 1 > result:
                for _, x in sorted(index[a] + index[b]):
                    if x == a and (flag := total > 0):
                        total -= 1
                    elif x == b:
                        result = max(result, total + flag)
                        total += 1

        return result


class Solution2:
    def largestVariance(self, s: str) -> int:
        counter = Counter(s)
        global_max = 0

        for ch_maj, ch_min in permutations(counter.keys(), 2):
            if ch_maj == ch_min:
                continue
            maj_count, min_count = 0, 0
            rest_min = counter[ch_min]
            for ch in s:
                if ch == ch_maj:
                    maj_count += 1
                elif ch == ch_min:
                    min_count += 1
                    rest_min -= 1
                if min_count:
                    global_max = max(global_max, maj_count - min_count)
                if maj_count < min_count and rest_min:
                    maj_count, min_count = 0, 0

        return global_max


def main():
    sol = Solution()
    print('3 ===', sol.largestVariance("aababbb"))
    print('0 ===', sol.largestVariance('abcde'))


if __name__ == '__main__':
    main()
