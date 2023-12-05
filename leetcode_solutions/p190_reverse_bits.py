class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = ans * 2 + n % 2
            n //= 2
        return ans


class Solution1:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        return int(b[::-1] + '0' * (32 - len(b)), 2)


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.reverseBits(n=0b00000010100101000001111010011100) == 964176192
    print('OK')

    print('Test 2... ', end='')
    assert sol.reverseBits(n=0b11111111111111111111111111111101) == 3221225471
    print('OK')


if __name__ == '__main__':
    test()
