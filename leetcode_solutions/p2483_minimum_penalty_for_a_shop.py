class Solution:
    def bestClosingTime(self, customers: str) -> int:
        eq = 0
        res = len(customers)

        for i in range(res - 1, -1, -1):
            if customers[i] == 'Y':
                eq += 1
            elif eq:
                eq -= 1
            if not eq:
                res = i
        return res


def main():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.bestClosingTime(customers="YYNY") == 2
    print('ok')
    print('Test 2 ... ', end='')
    assert sol.bestClosingTime(customers="NNNNN") == 0
    print('ok')
    print('Test 3 ... ', end='')
    assert sol.bestClosingTime(customers="YYYY") == 4
    print('ok')


if __name__ == '__main__':
    main()
