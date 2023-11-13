from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l < r:
            m = (l + r) // 2
            if arr[m] > arr[m + 1]:
                r = m
            else:
                l = m + 1

        return l


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.peakIndexInMountainArray(arr=[0, 1, 0]) == 1
    print('OK')

    print('Test 2... ', end='')
    assert sol.peakIndexInMountainArray(arr=[0, 2, 1, 0]) == 1
    print('OK')

    print('Test 3... ', end='')
    assert sol.peakIndexInMountainArray(arr=[0, 10, 5, 2]) == 1
    print('OK')


if __name__ == '__main__':
    test()
