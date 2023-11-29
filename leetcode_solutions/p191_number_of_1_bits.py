class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


class Solution2:
    def hammingWeight(self, n: int) -> int:
        return sum((n >> i) & 1 for i in range(32))


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.hammingWeight(n=0b00000000000000000000000000001011) == 3
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.hammingWeight(n=0b00000000000000000000000010000000) == 1
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.hammingWeight(n=0b11111111111111111111111111111101) == 31
    print('ok')


if __name__ == '__main__':
    test()
