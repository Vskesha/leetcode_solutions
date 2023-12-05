class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber:
            res = (chr((columnNumber - 1) % 26 + 65)) + res
            columnNumber = (columnNumber - 1) // 26
        return res


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.convertToTitle(columnNumber=1) == 'A'
    print('OK')

    print('Test 2... ', end='')
    assert sol.convertToTitle(columnNumber=28) == 'AB'
    print('OK')

    print('Test 3... ', end='')
    assert sol.convertToTitle(columnNumber=701) == 'ZY'
    print('OK')


if __name__ == '__main__':
    test()
