class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal = 0
        counter = 0
        for c in s:
            if c == 'L':
                bal -= 1
            else:
                bal += 1
            if bal == 0:
                counter += 1
        return counter


def main():
    sol = Solution()
    print('4 ===', sol.balancedStringSplit(s="RLRRLLRLRL"))
    print('2 ===', sol.balancedStringSplit(s="RLRRRLLRLL"))
    print('1 ===', sol.balancedStringSplit(s="LLLLRRRR"))


if __name__ == '__main__':
    main()
