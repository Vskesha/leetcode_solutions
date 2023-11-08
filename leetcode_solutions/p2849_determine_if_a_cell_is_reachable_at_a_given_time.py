class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        m = max(abs(sx - fx), abs(sy - fy))
        return (m > 0 or t != 1) and t >= m


class Solution2:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return not t == 1
        return t >= max(abs(sx - fx), abs(sy - fy))


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.isReachableAtTime(sx=2, sy=4, fx=7, fy=7, t=6) is True
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.isReachableAtTime(sx=3, sy=1, fx=7, fy=3, t=3) is False
    print('ok')


if __name__ == '__main__':
    test()
