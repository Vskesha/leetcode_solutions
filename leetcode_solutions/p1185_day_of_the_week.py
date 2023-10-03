from datetime import date


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return date(year, month, day).strftime('%A')


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.dayOfTheWeek(day=31, month=8, year=2019) == 'Saturday'
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.dayOfTheWeek(day=18, month=7, year=1999) == 'Sunday'
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.dayOfTheWeek(day=15, month=8, year=1993) == 'Sunday'
    print('ok')


if __name__ == '__main__':
    test()
