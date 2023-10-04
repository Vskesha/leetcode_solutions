class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.bulbSwitch(3) == 1
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.bulbSwitch(0) == 0
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.bulbSwitch(1) == 1
    print('ok')


if __name__ == '__main__':
    test()
