import string
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min(
            [s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1]
        )


class Solution0:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        unique = {}

        for i, ch in enumerate(s):
            if ch in seen:
                continue
            elif ch in unique:
                del unique[ch]
                seen.add(ch)
            else:
                unique[ch] = i

        return min(unique.values()) if unique else -1


class Solution1:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        unique = [ch for ch in cnt if cnt[ch] == 1]
        return min(s.find(ch) for ch in unique) if unique else -1


class Solution2:
    def firstUniqChar(self, s: str) -> int:
        ans = len(s)
        for c in string.ascii_lowercase:
            if s.count(c) == 1:
                ans = min(ans, s.find(c))
        return -1 if ans == len(s) else ans


class Solution3:
    def firstUniqChar(self, s: str) -> int:
        try:
            return min(s.find(c) for c in string.ascii_lowercase if s.count(c) == 1)
        except ValueError:
            return -1


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.firstUniqChar(s="leetcode") == 0
    print("OK")

    print("Test 2... ", end="")
    assert sol.firstUniqChar(s="loveleetcode") == 2
    print("OK")

    print("Test 3... ", end="")
    assert sol.firstUniqChar(s="aabb") == -1
    print("OK")


if __name__ == "__main__":
    test()
