from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img[0]), len(img)
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                neibs = []
                for y in range(max(0, i - 1), min(n, i + 2)):
                    for x in range(max(0, j - 1), min(m, j + 2)):
                        neibs.append(img[y][x])
                res[i][j] = int(sum(neibs) / len(neibs))
        return res


class Solution2:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img[0]), len(img)
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                sm, cnt = 0, 0
                for y in range(max(0, i - 1), min(n, i + 2)):
                    for x in range(max(0, j - 1), min(m, j + 2)):
                        sm += img[y][x]
                        cnt += 1
                res[i][j] = int(sm / cnt)
        return res


def test():
    sol = Solution()

    print('Test 1... ', end='')
    for a, b in zip(sol.imageSmoother(img=[[1, 1, 1],
                                           [1, 0, 1],
                                           [1, 1, 1]]),
                    [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]):
        assert a == b
    print('OK')

    print('Test 2... ', end='')
    for a, b in zip(sol.imageSmoother(img=[[100, 200, 100],
                                           [200, 50, 200],
                                           [100, 200, 100]]),
                    [[137, 141, 137],
                     [141, 138, 141],
                     [137, 141, 137]]):
        assert a == b
    print('OK')


if __name__ == '__main__':
    test()
