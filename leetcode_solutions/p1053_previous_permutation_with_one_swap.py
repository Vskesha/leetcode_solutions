from bisect import bisect_left
from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        while i:
            i -= 1
            if arr[i] > arr[i + 1]:
                j = bisect_left(arr, arr[i], lo=i + 1) - 1
                j = bisect_left(arr, arr[j], lo=i + 1, hi=j)
                arr[i], arr[j] = arr[j], arr[i]
                return arr
        return arr


class Solution2:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        while i:
            i -= 1
            if arr[i] > arr[i + 1]:
                j = bisect_left(arr, arr[i], lo=i + 1) - 1
                while arr[j - 1] == arr[j]:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
                return arr
        return arr


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.prevPermOpt1(arr=[3, 2, 1]) == [3, 1, 2]
    print("OK")

    print("Test 2... ", end="")
    assert sol.prevPermOpt1(arr=[1, 1, 5]) == [1, 1, 5]
    print("OK")

    print("Test 3... ", end="")
    assert sol.prevPermOpt1(arr=[1, 9, 4, 6, 7]) == [1, 7, 4, 6, 9]
    print("OK")


if __name__ == "__main__":
    test()
