from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            row = [1]
            prev = res[-1]
            for j in range(i - 1):
                row.append(prev[j] + prev[j + 1])
            row.append(1)
            res.append(row)

        return res


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.generate(numRows=5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    print('ok')
    print('Test 2 ... ', end='')
    assert sol.generate(numRows=1) == [[1]]
    print('ok')


if __name__ == '__main__':
    test()
