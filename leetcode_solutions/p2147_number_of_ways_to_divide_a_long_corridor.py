class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7

        cnt = corridor.count('S')
        if not cnt or cnt % 2:
            return 0

        seats = [i for i, ch in enumerate(corridor) if ch == 'S']
        ans = 1
        for i in range(1, len(seats) - 1, 2):
            ans = ans * (seats[i + 1] - seats[i]) % mod

        return ans


class Solution1:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7
        cnt = corridor.count('S')
        if cnt % 2 or not cnt:
            return 0

        ways = []
        seat = True
        for i, ch in enumerate(corridor):
            if ch == 'S':
                seat = not seat
                if seat:
                    ways.append(1)
            elif ways and seat:
                ways[-1] += 1
        if ways:
            ways.pop()
        ans = 1
        for w in ways:
            ans = ans * w % mod

        return ans


class Solution2:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7
        cnt = corridor.count('S')
        if cnt % 2 or not cnt:
            return 0

        lc = len(corridor)
        i, seats, ways = 0, 0, []
        for _ in range(cnt // 2 - 1):
            while seats < 2:
                if corridor[i] == 'S':
                    seats += 1
                i += 1
            st = i - 1
            seats = 0
            while corridor[i] != 'S':
                i += 1
            ways.append(i - st)

        ans = 1
        for w in ways:
            ans = ans * w % mod

        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.numberOfWays(corridor="SSPPSPS") == 3
    print('OK')

    print('Test 2... ', end='')
    assert sol.numberOfWays(corridor="PPSPSP") == 1
    print('OK')

    print('Test 3... ', end='')
    assert sol.numberOfWays(corridor="S") == 0
    print('OK')


if __name__ == '__main__':
    test()
