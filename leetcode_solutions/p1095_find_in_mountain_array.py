# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, data: list):
        self.data = data

    def get(self, index: int) -> int:
        return self.data[index]

    def length(self) -> int:
        return len(self.data)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: MountainArray) -> int:

        l, r = 1, mountain_arr.length() - 2
        while l < r:
            m = (l + r) // 2
            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                l = m + 1
            else:
                r = m

        peak = l

        l, r = 0, peak
        while l < r:
            m = (l + r) // 2
            if mountain_arr.get(m) < target:
                l = m + 1
            else:
                r = m

        if mountain_arr.get(l) == target:
            return l

        l, r = peak, mountain_arr.length() - 1
        while l < r:
            m = (l + r) // 2
            if mountain_arr.get(m) > target:
                l = m + 1
            else:
                r = m

        if mountain_arr.get(l) == target:
            return l

        return - 1


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.findInMountainArray(mountain_arr=MountainArray([1, 2, 3, 4, 5, 3, 1]), target=3) == 2
    print('ok')

    print('Test 1 ... ', end='')
    assert sol.findInMountainArray(mountain_arr=MountainArray([0, 1, 2, 4, 2, 1]), target=3) == -1
    print('ok')


if __name__ == '__main__':
    test()
