bad = 0


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l


def test():
    global bad
    sol = Solution()

    print('Test 1... ', end='')
    bad = 4
    assert sol.firstBadVersion(n=5) == 4
    print('OK')

    print('Test 2... ', end='')
    bad = 1
    assert sol.firstBadVersion(n=1) == 1
    print('OK')


if __name__ == '__main__':
    test()
