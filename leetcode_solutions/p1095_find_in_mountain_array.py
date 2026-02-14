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
    def findInMountainArray(
        self, target: int, mountain_arr: MountainArray
    ) -> int:

        left, right = 1, mountain_arr.length() - 2
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        left, right = 0, peak
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid

        if mountain_arr.get(left) == target:
            return left

        left, right = peak, mountain_arr.length() - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                right = mid

        if mountain_arr.get(left) == target:
            return left

        return -1


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert (
        sol.findInMountainArray(
            mountain_arr=MountainArray([1, 2, 3, 4, 5, 3, 1]), target=3
        )
        == 2
    )
    print("ok")

    print("Test 1 ... ", end="")
    assert (
        sol.findInMountainArray(
            mountain_arr=MountainArray([0, 1, 2, 4, 2, 1]), target=3
        )
        == -1
    )
    print("ok")


if __name__ == "__main__":
    test()
