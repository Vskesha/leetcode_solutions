class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber:
            res = (chr((columnNumber - 1) % 26 + 65)) + res
            columnNumber = (columnNumber - 1) // 26
        return res


def main():
    sol = Solution()
    print('A ===', sol.convertToTitle(1))
    print('AB ===', sol.convertToTitle(28))
    print('ZY ===', sol.convertToTitle(701))


if __name__ == '__main__':
    main()
