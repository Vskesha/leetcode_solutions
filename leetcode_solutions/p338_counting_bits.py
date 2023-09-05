class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = bin(i).count('1')
        return res


class Solution1:
    def countBits(self, n: int) -> list[int]:
        res = [0, 1, 1, 2]
        for i in range(4, n + 1, 4):
            val = bin(i).count('1')
            res.append(val)
            res.append(val + 1)
            res.append(val + 1)
            res.append(val + 2)
        while len(res) > n + 1:
            res.pop()
        return res


class Solution2:
    def countBits(self, n: int) -> list[int]:
        res = [0] * (n + 1)
        i = (len(bin(n)) - 2)
        i &= ~1

        def dp(st, i):
            if i < 0:
                return
            iv = 2 ** i
            for j in range(1, 5):
                pos = st + iv * (j - 1)
                if pos > n:
                    return
                res[pos] = res[st] + j // 2
                dp(pos, i - 2)

        dp(0, i)
        return res


class Solution3:
    def countBits(self, n: int) -> list[int]:
        res = [0]
        bits = [0] * (len(bin(n)) - 2)
        for i in range(1, n + 1):
            j = 0
            while bits[j]:
                bits[j] = 0
                j += 1
            bits[j] = 1
            res.append(res[-1] + 1 - j)
        return res


def main():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.countBits(n=2) == [0, 1, 1]
    print('ok')
    print('Test 2 ... ', end='')
    assert sol.countBits(n=5) == [0, 1, 1, 2, 1, 2]
    print('ok')
    print('Test 3 ... ', end='')
    assert sol.countBits(n=25) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3]
    print('ok')


if __name__ == '__main__':
    main()
