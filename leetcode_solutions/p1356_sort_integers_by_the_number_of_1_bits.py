from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1, 2, 4, 8, 3, 5, 6, 7]
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512,
                                                                                 1024]
    print('ok')


if __name__ == '__main__':
    test()
